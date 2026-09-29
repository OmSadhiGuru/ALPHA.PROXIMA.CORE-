"""Authoring/transport tests use disposable vaults, never the personal Vault."""
import concurrent.futures
import json
from pathlib import Path
import tempfile
import threading
import unittest
import urllib.error
import urllib.request

import unified_app as app


class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.memory = app.Memory(self.tmp.name)
        self.payload = dict(title='Une idée : mémoire', body='Écrit une fois.\n[[Autre note]]', kind='idea', request_id='a' * 32)

    def test_persists_markdown_and_reads_same_file(self):
        result = self.memory.capture(self.payload)
        note = self.memory.read(result['path'])['text']
        self.assertIn('Écrit une fois.', note)
        self.assertIn('status: "intake"', note)
        self.assertIn('authors: ["Founder"]', note)
        self.assertEqual(len(list(Path(self.tmp.name).rglob('*.md'))), 1)

    def test_concurrent_retries_create_one_note(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda _: self.memory.capture(self.payload), range(8)))
        self.assertEqual(len({r['path'] for r in results}), 1)
        self.assertEqual(len(list(Path(self.tmp.name).rglob('*.md'))), 1)

    def test_retry_cannot_change_existing_note(self):
        result = self.memory.capture(self.payload)
        with self.assertRaises(ValueError):
            self.memory.capture({**self.payload, 'body': 'Changed'})
        self.assertIn('Écrit une fois.', self.memory.read(result['path'])['text'])

    def test_rejects_path_escape_and_frontmatter_injection(self):
        for change in ({'request_id':'../../escape'}, {'title':'Hello\nstatus: ratified'}, {'body':''}, {'kind':'ratify'}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.memory.capture({**self.payload, **change})
        for path in ('../outside.md', '/etc/passwd', '.secret.md'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.memory.read(path)

    def test_rejects_symlink_destination(self):
        with tempfile.TemporaryDirectory() as outside:
            directory=Path(self.tmp.name)/app.CAPTURE_DIR
            directory.parent.mkdir(parents=True)
            directory.symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                self.memory.capture(self.payload)
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_saved_note_immediately_appears_in_shared_index(self):
        self.memory.view={'know':{'entries':[], 'note_count':0}}
        result=self.memory.capture(self.payload)
        self.assertEqual(self.memory.view['know']['entries'][0]['path'],result['path'])
        self.assertEqual(self.memory.view['know']['note_count'],1)

    def test_project_progress_persists_and_stale_edit_is_rejected(self):
        result = self.memory.capture({**self.payload, 'kind':'project', 'body':'Objectif\n- [ ] Première étape'})
        before = self.memory.read(result['path'])
        edit = dict(path=result['path'], version=before['version'], status='active', body=before['body'].replace('- [ ]', '- [x]'))
        after = self.memory.update(edit)
        self.assertEqual(after['status'], 'active')
        self.assertIn('- [x] Première étape', after['body'])
        self.assertNotEqual(before['version'], after['version'])
        with self.assertRaises(ValueError):
            self.memory.update(edit)
        self.assertIn('- [x]', self.memory.read(result['path'])['body'])

    def test_cannot_update_existing_institutional_document(self):
        with self.assertRaises(ValueError):
            self.memory.update(dict(path='00_CONSTITUTION/Book I.md', version='x', body='Replacement',status='active'))

    def test_external_note_edit_is_not_overwritten(self):
        result=self.memory.capture({**self.payload, 'kind':'project'})
        original=self.memory.read(result['path'])
        path=Path(self.tmp.name)/result['path']
        path.write_text(original['text']+'\nExternal Obsidian edit\n')
        with self.assertRaises(ValueError):
            self.memory.update(dict(path=result['path'],version=original['version'],body=original['body'],status='active'))
        self.assertIn('External Obsidian edit',path.read_text())

    def test_integration_evidence_distinguishes_import_from_live_connection(self):
        manifest = Path(self.tmp.name) / app.POCKET_MANIFEST
        manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({'records': [
            {'recording_id': 'one', 'recorded_at_utc': '2026-09-20T01:00:00Z'},
            {'recording_id': 'two', 'recorded_at_utc': '2026-09-21T01:00:00Z'},
        ]}))
        evidence = {item['id']: item for item in app.integration_evidence(self.tmp.name)}
        self.assertEqual(evidence['pocket-omi']['status'], 'imported')
        self.assertFalse(evidence['pocket-omi']['live'])
        self.assertEqual(evidence['pocket-omi']['evidence']['recording_count'], 2)
        self.assertEqual(evidence['voice-capture']['status'], 'local_ready')
        self.assertTrue(evidence['voice-capture']['live'])
        self.assertFalse(evidence['semantic-memory']['evidence']['vector_index'])
        self.assertEqual(evidence['google-calendar']['status'], 'authorization_required')


class TransportTests(CaptureTests):
    def setUp(self):
        super().setUp()
        self.server=app.make_server(self.memory,'127.0.0.1',0,token='test-private-token')
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True)
        self.thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.url='http://127.0.0.1:'+str(self.server.server_port)

    def request(self,path,body=None,**headers):
        request=urllib.request.Request(self.url+path, data=json.dumps(body).encode() if body is not None else None,headers=headers)
        try:
            response=urllib.request.urlopen(request,timeout=4)
        except urllib.error.HTTPError as error:
            response=error
        return response.status,response.read()

    def test_authentication_covers_page_session_and_capture(self):
        for path in ('/','/api/session','/universe/index.html'):
            self.assertEqual(self.request(path)[0],401)
        self.assertEqual(self.request('/api/capture',self.payload)[0],401)

    def test_csrf_and_origin_gate_capture(self):
        headers={'Authorization':'Bearer test-private-token','Content-Type':'application/json'}
        status,data=self.request('/api/session',**headers)
        self.assertEqual(status,200)
        self.assertEqual(self.request('/api/capture',self.payload,**headers)[0],403)
        headers['X-Alpha-CSRF']=json.loads(data)['csrf']
        self.assertEqual(self.request('/api/capture',self.payload,Origin='https://wrong.example',**headers)[0],403)
        status,data=self.request('/api/capture',self.payload,Origin=self.url,**headers)
        self.assertEqual(status,201)
        result=json.loads(data)
        self.assertTrue((Path(self.tmp.name)/result['path']).exists())


if __name__=='__main__':
    unittest.main()
