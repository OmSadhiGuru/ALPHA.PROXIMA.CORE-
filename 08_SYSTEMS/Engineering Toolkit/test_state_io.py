"""Failure-injection contracts for atomic publication of institutional state."""
import json
import os
import stat
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import state_io
import founder_os
import council_kernel


class AtomicStateTests(unittest.TestCase):
    def test_reader_observes_old_snapshot_until_replace_then_complete_new_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'state.json'
            path.write_text('{"version": 1}\n')
            path.chmod(0o640)
            replace = os.replace
            def inspect(source, destination):
                self.assertEqual(json.loads(path.read_text()), {'version': 1})
                self.assertEqual(json.loads(Path(source).read_text()), {'version': 2, 'text': 'éthique'})
                self.assertEqual(Path(source).parent, path.resolve().parent)
                replace(source, destination)
            with patch.object(state_io.os, 'replace', side_effect=inspect):
                state_io.write_json_atomic(path, {'version': 2, 'text': 'éthique'})
            self.assertEqual(json.loads(path.read_text())['version'], 2)
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o640)
            self.assertEqual(list(Path(tmp).iterdir()), [path])

    def test_failure_before_replace_preserves_original_and_removes_scratch(self):
        for operation in ('fsync', 'replace'):
            with self.subTest(operation=operation), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'state.json'
                old = b'{"original":true}\n'
                path.write_bytes(old)
                with patch.object(state_io.os, operation, side_effect=OSError('injected failure')):
                    with self.assertRaises(OSError):
                        state_io.write_json_atomic(path, {'new': True})
                self.assertEqual(path.read_bytes(), old)
                self.assertEqual(list(Path(tmp).iterdir()), [path])

    def test_unserializable_state_does_not_touch_existing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'state.json'
            path.write_text('{}\n')
            with self.assertRaises(TypeError):
                state_io.write_json_atomic(path, {'bad': object()})
            self.assertEqual(path.read_text(), '{}\n')
            self.assertEqual(list(Path(tmp).iterdir()), [path])

    def test_symlink_keeps_target_and_is_not_replaced(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'canonical.json'
            target.write_text('{}\n')
            link = Path(tmp) / 'alias.json'
            link.symlink_to(target)
            state_io.write_json_atomic(link, {'new': True})
            self.assertTrue(link.is_symlink())
            self.assertEqual(json.loads(target.read_text()), {'new': True})

    def test_new_state_has_private_permissions(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'nested/state.json'
            state_io.write_json_atomic(path, {'new': True})
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)

    def test_both_state_owners_preserve_valid_disk_state_on_failed_publication(self):
        for module, save, load in ((founder_os, founder_os.save_state, founder_os.load_state),
                                   (council_kernel, council_kernel.save, council_kernel.load)):
            with self.subTest(module=module.__name__), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'state.json'
                state = module.empty_state()
                save(state, path)
                old = path.read_bytes()
                with patch.object(module.state_io.os, 'replace', side_effect=OSError('injected')):
                    with self.assertRaises(OSError):
                        save(state, path)
                self.assertEqual(path.read_bytes(), old)
                load(path)  # Existing institutional schema must remain valid.
                self.assertEqual(list(Path(tmp).iterdir()), [path])


if __name__ == '__main__':
    unittest.main()
