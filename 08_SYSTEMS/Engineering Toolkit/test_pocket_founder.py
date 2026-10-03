"""Canonical sanitized Pocket -> Founder review proof. Never asserts LIVE.

Run with unittest discovery; all writes are in a TemporaryDirectory.
"""
from __future__ import annotations

import copy
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import alpha_adapters as adapters
import alpha_context as context
import alpha_events as events
import alpha_live as live
import founder_os as founder


class PocketFounderProof(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ledger = events.EventLedger(self.root / 'ledger.jsonl')
        self.registry = adapters.AdapterRegistry(self.root / 'registry.json')
        self.state = founder.load_state(founder.DEFAULT_STATE)
        self.before = copy.deepcopy(self.state)
        self.delivery = json.loads((adapters.VAULT_ROOT /
            '13_OPERATIONS/Live Integration Layer/fixtures/pocket_ai/capture.created.json').read_text())
        self.delivery.update(provider='pocket_ai', origin='fixture')
        self.ingestion = self.registry.ingest(self.delivery, self.ledger)
        self.capture = self.ledger.read_all()[0]

    def review(self, classification='founder_decision', reviewed=True, event_id=None):
        return founder.review_pocket_capture(
            self.state, self.ledger, event_id or self.capture['event_id'],
            classification=classification, founder_reviewed=reviewed)

    def test_context_normalization_and_provider_provenance(self):
        item = adapters.PocketAIAdapter().context_item('capture.created', self.delivery['payload'])
        self.assertEqual(context.validate(item), [])
        self.assertEqual(item['provider_item_id'], 'pai-cap-77b0')
        self.assertEqual(self.capture['occurred_at'], item['occurred_at'])
        self.assertEqual(self.capture['metadata']['provider_event_id'], item['provider_item_id'])
        self.assertFalse(self.ingestion['verified'])
        row = next(a for a in self.registry.view()['adapters'] if a['adapter_id'] == 'ADP-POCKET-AI')
        self.assertEqual(row['status'], 'disconnected')

    def test_route_event_synthesis_and_open_founder_decision(self):
        outcome = self.review()
        receipt = self.ledger.read_all()[-1]
        self.assertEqual(receipt['causation_id'], self.capture['event_id'])
        self.assertEqual(receipt['correlation_id'], self.capture['correlation_id'])
        self.assertEqual(receipt['metadata']['route'], 'LUMIAION -> JERANIUM -> LUMIAION')
        self.assertEqual(outcome['result']['synthesis_mode'], 'deterministic_review_receipt')
        decision = self.state['decisions'][-1]
        self.assertEqual(decision['status'], 'open')
        self.assertEqual(decision['requested_by'], 'LUMIAION')
        self.assertEqual(self.state['handoffs'][-1]['state'], 'review')
        self.assertEqual(live.evaluate_notification(receipt)['effective_severity'], 'action')
        for collection in ('tasks', 'priorities', 'agents', 'agent_runs', 'integrations'):
            self.assertEqual(self.state[collection], self.before[collection])
        founder.validate_state(self.state)

    def test_raw_provider_content_never_enters_ledger_or_state(self):
        delivery = copy.deepcopy(self.delivery)
        delivery['payload']['transcript'] = 'PRIVATE_BODY_SENTINEL_7F9'
        delivery['payload']['summary_text'] = 'PRIVATE_SUMMARY_SENTINEL_7F9'
        delivery['payload']['messages'] = [{'body': 'PRIVATE_MESSAGE_SENTINEL_7F9'}]
        self.registry.ingest(delivery, self.ledger)
        self.review()
        persisted = self.ledger.path.read_text() + json.dumps(self.state)
        for sentinel in ('PRIVATE_BODY_SENTINEL_7F9', 'PRIVATE_SUMMARY_SENTINEL_7F9',
                         'PRIVATE_MESSAGE_SENTINEL_7F9'):
            self.assertNotIn(sentinel, persisted)
        derived = json.dumps(self.ledger.read_all()[1:]) + json.dumps({
            k: self.state[k][len(self.before[k]):] for k in ('results', 'context_items', 'decisions', 'handoffs')})
        self.assertNotIn(self.delivery['payload']['title'], derived)
        self.assertNotIn(self.delivery['payload']['url'], derived)
        self.assertFalse(context.body_leaks(self.ledger.read_all()))

    def test_duplicate_delivery_and_promotion_across_restart(self):
        again = self.registry.ingest(self.delivery, self.ledger)
        self.assertEqual((again['stored'], again['duplicates']), (0, 1))
        self.review()
        path = self.root / 'state.json'
        founder.save_state(self.state, path)
        self.state = founder.load_state(path)
        self.ledger = events.EventLedger(self.ledger.path)
        before = copy.deepcopy(self.state)
        self.assertEqual(self.review()['status'], 'duplicate')
        self.assertEqual(self.state, before)
        self.assertEqual(len(self.ledger.read_all()), 2)

    def test_transcript_ready_cannot_double_promote_same_provider_item(self):
        self.review()
        delivery = dict(self.delivery, kind='transcript.ready')
        self.registry.ingest(delivery, self.ledger)
        transcript = self.ledger.read_all()[-1]
        self.assertEqual(self.review(event_id=transcript['event_id'])['status'], 'duplicate')
        self.assertEqual(len(self.state['results']), len(self.before['results']) + 1)

    def test_state_save_failure_reuses_ledger_receipt(self):
        self.review()
        receipt_id = self.ledger.read_all()[-1]['event_id']
        self.state = copy.deepcopy(self.before)  # Simulate failed save / restart.
        self.ledger = events.EventLedger(self.ledger.path)
        result = self.review()['result']
        self.assertEqual(result['provenance']['review_event_id'], receipt_id)
        self.assertEqual(len(self.ledger.read_all()), 2)

    def test_append_failure_does_not_mutate_founder_state(self):
        with patch.object(self.ledger, 'append', side_effect=OSError('disk unavailable')):
            with self.assertRaises(OSError):
                self.review()
        self.assertEqual(self.state, self.before)

    def test_unreviewed_and_irrelevant_signals_are_suppressed(self):
        for classification, reviewed in [('founder_decision', False), ('none', True), ('irrelevant', True)]:
            with self.subTest(classification=classification):
                self.assertEqual(self.review(classification, reviewed)['status'], 'suppressed')
                self.assertEqual(self.state, self.before)
                self.assertEqual(len(self.ledger.read_all()), 1)
        self.assertEqual(live.evaluate_notification(self.capture)['channels'], ['feed'])

    def test_reference_does_not_escalate(self):
        self.review('reference')
        self.assertEqual(self.state['decisions'], self.before['decisions'])
        self.assertFalse(self.ledger.read_all()[-1]['requires_founder'])

    def test_provider_suggestion_does_not_authorize_a_review(self):
        self.capture['metadata']['suggested_kind'] = 'decision'
        self.capture['metadata']['category'] = 'urgent'
        self.ledger.path.write_text(json.dumps(self.capture) + '\n')
        self.assertEqual(self.review(reviewed=False)['status'], 'suppressed')
        self.assertEqual(self.state, self.before)

    def test_reject_unknown_or_incomplete_provenance(self):
        with self.assertRaises(founder.StateError):
            self.review(event_id='not-in-ledger')
        self.capture['metadata'].pop('provider_event_id')
        self.ledger.path.write_text(json.dumps(self.capture) + '\n')
        with self.assertRaises(founder.StateError):
            self.review()
        self.assertEqual(self.state, self.before)

    def test_reject_body_in_contaminated_ledger(self):
        self.capture['metadata']['transcript'] = 'PRIVATE_SENTINEL'
        self.ledger.path.write_text(json.dumps(self.capture) + '\n')
        with self.assertRaises(founder.StateError):
            self.review()
        self.assertEqual(self.state, self.before)

    def test_no_fabricated_or_blocked_agent_route(self):
        for name in ('LUMIAION', 'JERANIUM'):
            self.state = copy.deepcopy(self.before)
            next(a for a in self.state['agents'] if a['name'] == name)['status'] = 'blocked'
            with self.assertRaises(founder.StateError):
                self.review()
        self.assertEqual(len(self.ledger.read_all()), 1)

    def test_conflicting_reclassification_is_not_a_second_decision(self):
        self.review('reference')
        before = copy.deepcopy(self.state)
        with self.assertRaises(founder.StateError):
            self.review('founder_decision')
        self.assertEqual(self.state, before)

    def test_cli_persists_only_to_selected_state_without_rendering(self):
        path = self.root / 'founder.json'
        founder.save_state(self.state, path)
        with contextlib.redirect_stdout(io.StringIO()), patch.object(founder, 'render_all') as render:
            code = founder.main(['--state', str(path), 'capture-review', self.capture['event_id'],
                '--ledger', str(self.ledger.path), '--classification', 'founder_decision', '--founder-reviewed'])
        self.assertEqual(code, 0)
        render.assert_not_called()
        saved = founder.load_state(path)
        self.assertEqual(len(saved['decisions']), len(self.before['decisions']) + 1)


if __name__ == '__main__':
    unittest.main()
