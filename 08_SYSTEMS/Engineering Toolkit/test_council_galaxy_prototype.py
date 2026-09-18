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


if __name__ == '__main__':
    unittest.main()
