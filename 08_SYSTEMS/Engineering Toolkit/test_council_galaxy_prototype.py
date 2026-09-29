"""Institutional contracts for the read-only Galaxy projection."""
from __future__ import annotations

import copy
import json
import io
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import Mock
import shutil
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest.mock import patch

import council_galaxy_prototype as galaxy

ROOT = galaxy.VAULT_ROOT
REGISTRY = Path('13_OPERATIONS/AI Council/Agent and Subagent Registry.md')
COUNCIL = Path('13_OPERATIONS/AI Council/state/council-state.json')
FOUNDER = Path('13_OPERATIONS/Founder OS/state/founder-state.json')


def source_view():
    registry = galaxy.role_registry.load_roles(ROOT)
    return {'registry': registry, 'desks': copy.deepcopy(registry['roles'])}


def occupants(view):
    return ([view['center']] + [s['desk'] for s in view['inner_circle'] if not s['proposed']]
            + [d for c in view['council'] for d in [c['lead']] + c['constellation']]
            + view['unassigned'])


class GalaxyContracts(unittest.TestCase):
    def test_every_canonical_role_once_and_no_invented_agent(self):
        source = source_view()
        before = copy.deepcopy(source)
        view = galaxy.classify_roles(source)
        self.assertEqual(Counter(d['id'] for d in occupants(view)),
                         Counter(d['id'] for d in source['desks']))
        self.assertEqual(source, before)
        self.assertEqual(view['center']['id'], 'AGT-001')
        self.assertEqual({d['id'] for d in view['unassigned']},
                         {d['id'] for d in source['desks'] if d['operating_owner'] == 'Owner pending'})
        for seat in view['inner_circle']:
            if seat['proposed']:
                self.assertIsNone(seat['desk'])
                self.assertNotIn('id', seat)

    def test_missing_center_fails_without_fabrication(self):
        source = source_view()
        source['desks'] = [d for d in source['desks'] if d['id'] != 'AGT-001']
        with self.assertRaisesRegex(galaxy.PrototypeError, 'AGT-001'):
            galaxy.classify_roles(source)

    def test_registry_evolution_does_not_drop_or_duplicate_roles(self):
        for change in ('remove_steward', 'reassign_steward', 'add_role'):
            with self.subTest(change=change):
                source = source_view()
                desks = source['desks']
                if change == 'remove_steward':
                    desks[:] = [d for d in desks if d['id'] != 'AGT-009']
                elif change == 'reassign_steward':
                    next(d for d in desks if d['id'] == 'AGT-009')['operating_owner'] = 'Owner pending'
                else:
                    # Synthetic fixture only, never an institutional role.
                    desks.append(dict(desks[0], id='AGT-999', named_role='Fixture role'))
                owners = {}
                for d in desks:
                    owners.setdefault(d['operating_owner'], []).append(d['id'])
                source['registry']['owners'] = [{'owner': k, 'role_ids': v} for k, v in owners.items()]
                self.assertEqual(Counter(d['id'] for d in occupants(galaxy.classify_roles(source))),
                                 Counter(d['id'] for d in desks))

    def test_real_views_and_renders_preserve_all_institutional_inputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for relative in (REGISTRY, COUNCIL, FOUNDER):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            before = {p: (root / p).read_bytes() for p in (REGISTRY, COUNCIL, FOUNDER)}
            view = galaxy.build_galaxy_view(root)
            self.assertTrue(view['read_only'])
            output = root / 'render/galaxy.html'
            galaxy.write_output(view, galaxy.DEFAULT_TEMPLATE, output)
            office = galaxy.office_spatial
            office.write_output(office.build_office_view(root), office.DEFAULT_TEMPLATE, root / 'render/office.html')
            self.assertNotIn(galaxy.VIEW_PLACEHOLDER, output.read_text())
            self.assertIn('visual grouping with', output.read_text())
            self.assertNotIn('reports via', output.read_text())
            self.assertEqual(before, {p: (root / p).read_bytes() for p in before})

    def test_missing_council_state_cli_is_controlled_error(self):
        with tempfile.TemporaryDirectory() as tmp, redirect_stderr(io.StringIO()) as errors:
            self.assertEqual(galaxy.main(['--state', str(Path(tmp) / 'missing.json'), 'view']), 2)
            self.assertIn('State document not found', errors.getvalue())

    def test_spatial_http_surfaces_are_read_only_and_root_scoped(self):
        office = galaxy.office_spatial
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for relative in (REGISTRY, COUNCIL, FOUNDER):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            # An empty independent ledger distinguishes this root from the canonical one.
            (root / COUNCIL).write_text(json.dumps(office.council_kernel.empty_state()))
            before = {p: (root / p).read_bytes() for p in (REGISTRY, COUNCIL, FOUNDER)}
            for module, endpoint in ((office, '/api/v1/sessions'), (galaxy, '/api/galaxy')):
                with patch('http.server.HTTPServer') as server, redirect_stdout(io.StringIO()):
                    module.serve(root, module.DEFAULT_TEMPLATE)
                    handler_type = server.call_args.args[1]
                for method in ('do_POST', 'do_PUT', 'do_PATCH', 'do_DELETE'):
                    self.assertFalse(hasattr(handler_type, method), method)
                handler = handler_type.__new__(handler_type)
                handler.path = endpoint
                handler.headers = {}
                handler.wfile = io.BytesIO()
                handler.send_response = Mock()
                handler.send_header = Mock()
                handler.end_headers = Mock()
                handler.do_GET()
                handler.send_response.assert_called_once_with(200)
                payload = json.loads(handler.wfile.getvalue())
                ledger = payload if module is office else payload['council']
                self.assertEqual(ledger['counts']['active'], 0)
            self.assertEqual(before, {p: (root / p).read_bytes() for p in before})

    def test_renderer_escapes_data_and_rejects_missing_placeholder(self):
        with tempfile.TemporaryDirectory() as tmp:
            template = Path(tmp) / 'template.html'
            template.write_text('<script>' + galaxy.VIEW_PLACEHOLDER + '</script>')
            self.assertNotIn('</script><script>', galaxy.render_app({'x': '</script><script>'}, template))
            template.write_text('<html></html>')
            with self.assertRaises(galaxy.PrototypeError):
                galaxy.render_app({}, template)




class EdgeTaxonomyContracts(unittest.TestCase):
    """The rule this class exists to enforce: an inference never looks like canon."""

    def setUp(self):
        self.galaxy = galaxy.classify_roles(source_view())
        self.edges = galaxy.build_edges(self.galaxy)

    def node_ids(self):
        return {desk['id'] for desk in occupants(self.galaxy)} | {'VAULT'}

    def test_no_visible_node_is_left_orphaned(self):
        touched = {edge['source'] for edge in self.edges} | {edge['target'] for edge in self.edges}
        missing = self.node_ids() - touched
        self.assertEqual(missing, set(),
                         f"these seats would render unreachable: {sorted(missing)}")

    def test_every_edge_carries_its_type_authority_confidence_and_direction(self):
        for edge in self.edges:
            with self.subTest(edge=(edge['source'], edge['target'])):
                self.assertIn(edge['type'], galaxy.EDGE_TYPES)
                self.assertTrue(edge['authority'].strip(), 'an edge with no authority is a guess')
                self.assertIsInstance(edge['confidence'], float)
                self.assertIn(edge['direction'], ('directed', 'bidirectional'))
                self.assertTrue(edge['created_at'])

    def test_an_unknown_edge_type_is_refused(self):
        with self.assertRaises(galaxy.PrototypeError):
            galaxy.edge('A', 'B', 'vibes', authority='x', confidence=1.0)

    def test_confidence_outside_zero_to_one_is_refused(self):
        for value in (-0.1, 1.5):
            with self.subTest(confidence=value):
                with self.assertRaises(galaxy.PrototypeError):
                    galaxy.edge('A', 'B', 'semantic', authority='x', confidence=value)

    def test_a_structural_edge_asserts_nothing_and_says_so(self):
        structural = [edge for edge in self.edges if edge['type'] == 'structural']
        self.assertTrue(structural, 'unowned roles must still be reachable')
        for edge in structural:
            with self.subTest(edge=(edge['source'], edge['target'])):
                self.assertEqual(edge['confidence'], 0.0)
                self.assertTrue(edge['interpreted'])
                self.assertTrue(edge['note'].strip(),
                                'a navigation-only line must say that is all it is')

    def test_the_only_full_confidence_edges_are_the_ones_a_record_states(self):
        for edge in self.edges:
            if edge['confidence'] == 1.0:
                with self.subTest(edge=(edge['source'], edge['target'])):
                    self.assertFalse(edge['interpreted'])
                    self.assertIn(edge['type'], ('semantic', 'operational'))

    def test_no_edge_claims_lumiaion_owns_a_department(self):
        # The registry names offices; it does not name a reporting line from
        # LUMIAION to them. The radial layout must not invent one.
        leads = {constellation['lead']['id'] for constellation in self.galaxy['council']}
        for edge in self.edges:
            if edge['source'] == self.galaxy['center']['id'] and edge['target'] in leads:
                with self.subTest(target=edge['target']):
                    self.assertEqual(edge['type'], 'structural')

    def test_the_vault_relationship_is_the_canonical_one(self):
        semantic = [edge for edge in self.edges if edge['type'] == 'semantic']
        self.assertEqual(len(semantic), 1)
        self.assertEqual({semantic[0]['source'], semantic[0]['target']},
                         {'VAULT', self.galaxy['center']['id']})
        self.assertIn('INT-001', semantic[0]['authority'])

    def test_no_event_derived_edge_is_fabricated_without_events(self):
        # `causal` and `temporal` edges may only come from the event ledger.
        # This composition reads the registry, so it must produce none.
        types = {edge['type'] for edge in self.edges}
        self.assertNotIn('causal', types)
        self.assertNotIn('temporal', types)

    def test_the_summary_counts_what_is_interpretation(self):
        summary = galaxy.edge_summary(self.edges)
        self.assertEqual(summary['total'], len(self.edges))
        self.assertEqual(summary['interpreted'] + summary['canonical'], summary['total'])
        self.assertEqual(sum(summary['counts'].values()), summary['total'])

    def test_the_view_publishes_the_graph_and_its_summary(self):
        view = galaxy.build_galaxy_view(ROOT)
        self.assertIn('edges', view)
        self.assertIn('edge_summary', view)
        self.assertEqual(view['edge_summary']['total'], len(view['edges']))


class SpatialInterfaceContracts(unittest.TestCase):
    """What the rendered page must still do, checked without a browser.

    These are text assertions on the template, which is a weak form of test —
    so each one targets a behavior whose *absence* would be a silent regression
    rather than a visible break: a dashed style quietly dropped, a thought path
    that stops truncating, an inference rendered as canon.
    """

    def setUp(self):
        self.template = galaxy.DEFAULT_TEMPLATE.read_text(encoding='utf-8')

    def test_the_page_draws_edges_from_the_view_rather_than_hardcoding_them(self):
        self.assertIn('(VIEW.edges || []).forEach(drawEdge)', self.template)

    def test_every_edge_type_in_the_taxonomy_has_a_visual_style(self):
        for edge_type in galaxy.EDGE_TYPES:
            if edge_type == 'inferred':
                self.assertIn('inferred:', self.template)
                continue
            self.assertIn(f'{edge_type}:', self.template)

    def test_an_interpreted_edge_is_forced_to_a_dashed_style(self):
        self.assertIn('record.interpreted ?', self.template)
        self.assertIn('LineDashedMaterial', self.template)
        # Three.js renders a dashed material solid without this call.
        self.assertIn('computeLineDistances()', self.template)

    def test_the_legend_declares_how_much_of_the_graph_is_interpretation(self):
        self.assertIn('interpretation, not canon', self.template)

    def test_the_thought_path_truncates_on_a_revisit_rather_than_looping(self):
        self.assertIn('thoughtPath.slice(0, existing + 1)', self.template)

    def test_the_thought_path_is_keyboard_navigable(self):
        self.assertIn('<button class="step', self.template)
        self.assertIn('window.stepBack', self.template)

    def test_selecting_a_node_focuses_the_camera_on_it(self):
        self.assertIn('applyFocus(id)', self.template)
        self.assertIn('FOCUS_SCALE', self.template)

    def test_unrelated_context_is_dimmed_rather_than_hidden(self):
        # Multiplying opacity keeps context visible; setting `visible = false`
        # would make every selection a fresh disorientation.
        self.assertIn('base * 0.3', self.template)
        self.assertNotIn('visible = false', self.template)

    def test_returning_to_the_overview_restores_the_whole_scene(self):
        self.assertIn('applyFocus(null)', self.template)

    def test_camera_movement_is_interpolated_and_respects_reduced_motion(self):
        self.assertIn('tweenTo_', self.template)
        self.assertIn('REDUCED_MOTION', self.template)

    def test_the_rendered_page_matches_the_template_behaviour(self):
        rendered = galaxy.DEFAULT_OUTPUT.read_text(encoding='utf-8')
        for marker in ('drawEdge', 'thoughtPath', 'applyFocus', 'renderEdgeLegend'):
            self.assertIn(marker, rendered,
                          f'{marker} is in the template but not the committed render')


class LiveOverlayContracts(unittest.TestCase):
    """Presence on top of structure, without either lying about the other."""

    def test_the_committed_render_carries_no_machine_local_telemetry(self):
        # `galaxy-prototype.html` is in the Foundation's permanent record.
        # Presence expires in three minutes; committing one would preserve a
        # moment of one developer's afternoon as though it were state.
        rendered = galaxy.DEFAULT_OUTPUT.read_text(encoding='utf-8')
        self.assertIn('Rendered without live state', rendered)
        payload = json.loads(rendered.split('const VIEW = ', 1)[1].split(';\nconst REDUCED', 1)[0])
        self.assertFalse(payload['live']['available'])
        self.assertEqual(payload['live']['presence'], [])
        self.assertEqual(payload['live']['activity'], [])
        self.assertEqual(payload['live']['badge'], 0)

    def test_a_static_render_says_it_is_static_rather_than_showing_nothing(self):
        # An interface that cannot distinguish "nothing happened" from "I cannot
        # see" is lying by omission.
        self.assertIn('static render', galaxy.LIVE_OMITTED['realtime']['detail'])
        self.assertTrue(galaxy.LIVE_OMITTED['realtime']['canonical_readable'])
        self.assertFalse(galaxy.LIVE_OMITTED['realtime']['presence_trustworthy'])

    def test_the_served_view_includes_live_state(self):
        view = galaxy.build_galaxy_view(ROOT, include_live=True)
        self.assertIn('live', view)
        self.assertIn('realtime', view['live'])

    def test_a_missing_live_layer_dims_presence_rather_than_breaking_the_scene(self):
        with patch.object(galaxy, '_load_sibling', side_effect=OSError('no ledger here')):
            section = galaxy.build_live_section()
        self.assertFalse(section['available'])
        self.assertIn('no ledger here', section['reason'])
        # The registry view must still be buildable and must still say the
        # Foundation's own knowledge is readable.
        self.assertTrue(section['realtime']['canonical_readable'])
        self.assertFalse(section['realtime']['presence_trustworthy'])

    def test_presence_never_reads_as_trustworthy_without_a_live_transport(self):
        section = galaxy.build_live_section()
        if section['realtime']['mode'] != 'live':
            self.assertFalse(section['realtime']['presence_trustworthy'])

    def test_the_live_section_reports_integration_counts_honestly(self):
        section = galaxy.build_live_section()
        if section['available']:
            counts = section['integration_counts']
            self.assertGreater(counts['total'], 0)
            # Nothing has been verified in this repository, so nothing is
            # connected. If this ever fails, a real delivery arrived.
            self.assertEqual(counts['connected'], 0)


class LiveOverlayInterfaceContracts(unittest.TestCase):
    def setUp(self):
        self.template = galaxy.DEFAULT_TEMPLATE.read_text(encoding='utf-8')

    def test_the_scene_honours_the_read_models_staleness_rather_than_recomputing_it(self):
        # Every client computing TTL arithmetic is every client getting it wrong
        # differently.
        self.assertIn("row.stale", self.template)
        self.assertNotIn('ttl_seconds', self.template)

    def test_an_expired_report_is_dimmed_and_never_pulsed(self):
        self.assertIn("classList.toggle('presence-stale'", self.template)
        self.assertIn('!row.stale &&', self.template)

    def test_presence_resolves_a_report_keyed_by_id_or_by_name(self):
        # An agent reports itself by the name it knows; the scene draws registry
        # ids. Forcing agents to learn ids would make presence silently empty.
        self.assertIn('function presenceFor(nodeId)', self.template)
        self.assertIn('row.node_id === name', self.template)

    def test_text_from_the_event_ledger_is_escaped_before_it_becomes_markup(self):
        self.assertIn('function escapeText(', self.template)
        for field in ('escapeText(event.title)', 'escapeText(row.state)'):
            self.assertIn(field, self.template)

    def test_the_page_only_refreshes_when_there_is_an_origin_to_ask(self):
        self.assertIn("window.location.protocol !== 'file:'", self.template)
        self.assertIn("'/api/v1/live'", self.template)

    def test_a_failed_refresh_keeps_the_last_known_state_and_says_so(self):
        self.assertIn('Lost contact with the live layer', self.template)

    def test_the_banner_distinguishes_unconfigured_from_degraded(self):
        # Nothing connected is not the same as something broken.
        self.assertIn("realtime.mode === 'stale' || realtime.mode === 'unavailable'", self.template)


class MemoryFieldContracts(unittest.TestCase):
    """The ledger joined to the registry, without either borrowing the other's authority."""

    def test_the_committed_render_carries_no_memory_graph(self):
        # Same reason presence is excluded: the ledger is machine-local runtime
        # state, and a committed artifact must not preserve one afternoon's
        # activity as though it were structure.
        rendered = galaxy.DEFAULT_OUTPUT.read_text(encoding='utf-8')
        payload = json.loads(rendered.split('const VIEW = ', 1)[1].split(';\nconst REDUCED', 1)[0])
        self.assertFalse(payload['memory']['available'])
        self.assertEqual(payload['memory']['nodes'], [])
        self.assertEqual(payload['memory']['edges'], [])
        self.assertIn('Serve this page', payload['memory']['reason'])

    def test_the_served_view_includes_the_memory_graph(self):
        view = galaxy.build_galaxy_view(ROOT, include_live=True)
        self.assertIn('memory', view)
        self.assertIn('edge_summary', view['memory'])

    def test_a_missing_ledger_dims_memory_without_breaking_the_registry_view(self):
        with patch.object(galaxy, '_load_sibling', side_effect=OSError('no ledger')):
            section = galaxy.build_memory_section(ROOT)
        self.assertFalse(section['available'])
        self.assertIn('no ledger', section['reason'])
        self.assertEqual(section['nodes'], [])
        # And the registry half is unaffected: it does not depend on occurrence.
        view = galaxy.build_galaxy_view(ROOT, include_live=False)
        self.assertGreater(len(view['edges']), 0)

    def test_the_registry_and_ledger_graphs_are_built_by_different_constructors(self):
        # The structural guarantee: the galaxy's own `edge` wrapper refuses the
        # ledger-only types, so this view cannot assert causation however its
        # code changes.
        for edge_type in ('causal', 'temporal'):
            with self.subTest(edge_type=edge_type):
                with self.assertRaises(galaxy.PrototypeError):
                    galaxy.edge('A', 'B', edge_type, authority='registry', confidence=1.0)

    def test_no_registry_edge_is_ever_causal_or_temporal(self):
        view = galaxy.build_galaxy_view(ROOT, include_live=False)
        for item in view['edges']:
            self.assertNotIn(item['type'], ('causal', 'temporal'))

    def test_memory_edges_are_witnessed_rather_than_interpreted(self):
        section = galaxy.build_memory_section(ROOT)
        if section['available']:
            self.assertEqual(section['edge_summary']['interpreted'], 0)

    def test_the_memory_section_reports_its_unresolved_actors(self):
        section = galaxy.build_memory_section(ROOT)
        self.assertIn('unresolved_actors', section)
        self.assertIn('actors_unresolved', section['counts'])


class MemoryFieldInterfaceContracts(unittest.TestCase):
    def setUp(self):
        self.template = galaxy.DEFAULT_TEMPLATE.read_text(encoding='utf-8')

    def test_memory_nodes_are_positioned_deterministically_from_their_id(self):
        # A graph that reshuffles on every load cannot be learned.
        self.assertIn('function hashAngle(id)', self.template)
        self.assertIn('hashAngle(node.id)', self.template)
        self.assertNotIn('Math.random()', self.template.split('hashAngle')[1][:400])

    def test_memory_nodes_are_placed_outside_the_council_ring(self):
        # The Council is who exists; memory is what happened. Overlapping them
        # would make an event look like an institution.
        self.assertIn("const radius = entity ? 30 : 25.5", self.template)

    def test_memory_edges_go_through_the_same_renderer_as_registry_edges(self):
        # One visual grammar. `drawEdge` does not know which builder produced an
        # edge, which is the point of sharing the taxonomy.
        self.assertIn('(memory.edges || []).forEach(drawEdge)', self.template)

    def test_only_entities_awaiting_the_founder_are_labelled_at_rest(self):
        self.assertIn("attention ? 'overview' : 'hover'", self.template)

    def test_labelling_waits_until_the_label_layer_exists(self):
        # The ordering bug this guards against threw on every load with a
        # non-empty ledger, and was invisible in a static render.
        body = self.template
        self.assertIn('function labelMemoryNodes()', body)
        self.assertLess(body.index('labelMemoryNodes();'), body.index('updateLabelVisibility();\n\n  // The live overlay'))
        self.assertGreater(body.index('labelMemoryNodes();'), body.index('const labels = []'))

    def test_an_entity_panel_shows_its_whole_timeline(self):
        self.assertIn("node.timeline || []", self.template)
        self.assertIn('<b>Timeline</b>', self.template)

    def test_every_connection_names_the_record_supporting_it(self):
        self.assertIn('escapeText(e.authority)', self.template)

    def test_an_unresolved_actor_panel_refuses_to_guess_a_seat(self):
        # Asserted on phrases that are contiguous in the *source*: the panel
        # builds its prose by concatenation, so a sentence spanning two string
        # literals is not findable here even though it renders correctly. The
        # rendered wording is covered by the DOM harness instead.
        self.assertIn('No Council seat', self.template)
        self.assertIn('matching one by resemblance', self.template)

    def test_ledger_text_reaching_the_panel_is_escaped(self):
        for field in ('escapeText(node.label)', 'escapeText(step.title)',
                      'escapeText(step.event_type)', 'escapeText(node.entity_type)'):
            with self.subTest(field=field):
                self.assertIn(field, self.template)

    def test_memory_nodes_are_selectable_and_join_the_thought_path(self):
        self.assertIn('selectMemoryNode(id)', self.template)
        self.assertIn("pushThought('memory', id)", self.template)
        self.assertIn("step.kind === 'memory'", self.template)

    def test_the_legend_counts_both_graphs_so_every_line_has_a_key(self):
        self.assertIn('const total = type =>', self.template)
        self.assertIn('witnessed by the event ledger', self.template)

    def test_the_rendered_page_carries_the_memory_behaviour(self):
        rendered = galaxy.DEFAULT_OUTPUT.read_text(encoding='utf-8')
        for marker in ('labelMemoryNodes', 'selectMemoryNode', 'openMemoryPanel', 'hashAngle'):
            self.assertIn(marker, rendered)


if __name__ == '__main__':
    unittest.main()
