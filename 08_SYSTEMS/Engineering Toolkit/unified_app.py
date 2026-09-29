#!/usr/bin/env python3
"""One application over an explicitly selected Vault, with explicit authoring.

Founder/Council engines remain the sole writers of their operational state.
The capture endpoint creates authored intake notes, never institutional approval.
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import mimetypes
import os
from pathlib import Path
import re
import secrets
import tempfile
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlsplit

import alpha_app
import council_galaxy_prototype as galaxy
import office_spatial

APP = Path(__file__).resolve().parents[2] / '13_OPERATIONS/Alpha Proxima App'
CAPTURE_DIR = Path('14_FUTURE/Founder Ideas')
POCKET_MANIFEST = Path('Pocket/Imports/2026-09-22/Sources/manifest.json')


def integration_evidence(root):
    """Report observed capabilities without promoting plans to connections."""
    root = Path(root)
    manifest_path = root / POCKET_MANIFEST
    pocket_records = 0
    pocket_latest = None
    if manifest_path.is_file():
        try:
            records = json.loads(manifest_path.read_text(encoding='utf-8')).get('records', [])
            if isinstance(records, list):
                pocket_records = len(records)
                dates = [record.get('recorded_at_utc') for record in records
                         if isinstance(record, dict) and record.get('recorded_at_utc')]
                pocket_latest = max(dates, default=None)
        except (OSError, ValueError, TypeError):
            pass

    return [
        {
            'id': 'pocket-omi', 'name': 'Pocket AI + OMI',
            'status': 'imported' if pocket_records else 'authorization_required',
            'live': False,
            'detail': (f'{pocket_records} enregistrements Pocket sont archivés dans le Vault; '
                       'la synchronisation Pocket/OMI en direct exige encore un connecteur autorisé.'
                       if pocket_records else
                       'Aucune archive Pocket locale ni connexion OMI autorisée n’est détectée.'),
            'evidence': {'manifest': POCKET_MANIFEST.as_posix() if pocket_records else None,
                         'recording_count': pocket_records, 'latest_recording_at': pocket_latest},
        },
        {
            'id': 'voice-capture', 'name': 'Voice capture', 'status': 'local_ready', 'live': True,
            'detail': 'La saisie locale authentifiée écrit des notes intake dans le Vault; les transcriptions Pocket historiques sont consultables.',
            'evidence': {'endpoint': '/api/capture', 'destination': CAPTURE_DIR.as_posix()},
        },
        {
            'id': 'chatgpt-codex', 'name': 'ChatGPT / Codex', 'status': 'repository_transport', 'live': False,
            'detail': 'Le transport vérifié reste Git/PR. Aucun canal d’exécution ChatGPT/Codex direct n’est exposé par Founder OS.',
            'evidence': {'transport': 'git_pull_request'},
        },
        {
            'id': 'google-calendar', 'name': 'Google Calendar', 'status': 'authorization_required', 'live': False,
            'detail': 'Aucun OAuth Google Calendar autorisé n’est disponible dans cette application.',
            'evidence': {'required': 'google_calendar_oauth'},
        },
        {
            'id': 'semantic-memory', 'name': 'Semantic memory', 'status': 'structural_only', 'live': False,
            'detail': 'La recherche titre/chemin/métadonnées fonctionne. Aucun index vectoriel ou moteur d’embeddings n’est configuré.',
            'evidence': {'structural_index': True, 'vector_index': False},
        },
        {
            'id': 'health-performance', 'name': 'Health / performance', 'status': 'source_required', 'live': False,
            'detail': 'ATHENA est enregistrée, mais aucune source HealthKit ou export santé n’est connectée à cette application.',
            'evidence': {'owner': 'ATHENA', 'data_source': None},
        },
        {
            'id': 'financial-systems', 'name': 'Financial systems', 'status': 'source_required', 'live': False,
            'detail': 'VORTEX est enregistré, mais aucun compte financier ni flux de marché n’est connecté à Founder OS.',
            'evidence': {'owner': 'VORTEX', 'data_source': None},
        },
    ]


class NotReady(Exception):
    pass


class Memory:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.lock = threading.Lock()
        self.capture_lock = threading.Lock()
        self.view = None
        self.updated = 0
        self.generation = 0
        self.running = False
        self.error = None
        self.contract = None

    def refresh(self):
        with self.lock:
            if self.running or (self.view and time.monotonic() - self.updated < 20):
                return
            self.running = True
            generation = self.generation

        def build():
            try:
                state = alpha_app.founder_os.load_state(self.root / '13_OPERATIONS/Founder OS/state/founder-state.json')
                notes, unavailable = [], []
                for path in alpha_app.vault_validator.markdown_files(self.root, False):
                    relative = path.relative_to(self.root).as_posix()
                    try:
                        placeholder = getattr(path.stat(), 'st_flags', 0) & 0x40000000
                        text = None if placeholder else path.read_text(encoding='utf-8', errors='replace')
                    except OSError:
                        # iCloud may time out while a placeholder is recalled.
                        # Preserve the path as unavailable; never turn absence
                        # into an indexed note or make the whole app unusable.
                        unavailable.append(relative)
                        continue
                    if placeholder:
                        unavailable.append(relative)
                        continue
                    present, front, body, errors = alpha_app.vault_validator.parse_frontmatter(text)
                    notes.append(alpha_app.vault_validator.Note(path, relative, text, body, front, errors, present))
                view = alpha_app.build_app_view(state, self.root, notes=notes)
                contract = alpha_app.truth_kernel.build(self.root, notes=notes)
                view['unavailable_notes'] = unavailable
                view['knowledge_complete'] = not unavailable
                view['integration_evidence'] = integration_evidence(self.root)
                contract['coverage'] = {'complete':not unavailable, 'unavailable_count':len(unavailable)}
                # The same canonical source powers every presentation.
                view['source'] = {'vault': str(self.root), 'mode': 'live_vault'}
                with self.lock:
                    if generation == self.generation:
                        self.view = view
                        self.contract = contract
                        self.updated = time.monotonic()
                    self.error = None
            except Exception as exc:
                with self.lock:
                    self.error = type(exc).__name__ + ': ' + str(exc)
            finally:
                with self.lock:
                    self.running = False
        threading.Thread(target=build, daemon=True).start()

    def get(self):
        self.refresh()
        with self.lock:
            if self.view is None:
                raise NotReady(self.error or 'Lecture du Vault en cours. Réessaie dans quelques secondes.')
            return {**self.view, 'refreshing': self.running, 'refresh_error': self.error}

    def brain(self):
        view = self.get()
        know = view['know']
        kernel = know['truth_kernel']
        summary = {'note_count': know['note_count'], 'domain_count':len(know['domains']),
                'connectedness':know['coherence']['connectedness'],
                'coherence_defects':sum(know['coherence']['counts'].values()),
                'knowledge_nodes':kernel['counts']['nodes'],
                'knowledge_findings':kernel['health']['counts']['findings'],
                'health_status':kernel['health']['status'] if view.get('knowledge_complete',True) else 'partial',
                'unavailable_notes':len(view.get('unavailable_notes', []))}
        contract = self.contract
        if contract is None:
            raise NotReady('Lecture du Vault en cours.')
        return {**summary, 'virtual_brain': self._council_brain_projection(contract, view)}

    @staticmethod
    def _council_brain_projection(contract, view, limit=96):
        """A compact, read-only graph for the Council's spatial memory view.

        The projection deliberately carries metadata and paths, not note bodies.
        It is derived afresh from the Truth Kernel and never becomes a second
        vault or an authority capable of recording Council decisions.
        """
        nodes = contract.get('nodes', [])
        links = contract.get('relationships', [])
        linked = {rel.get('source_node_id') for rel in links} | {rel.get('target_node_id') for rel in links}

        def category(node):
            path = node.get('source_path', '')
            return path.split('/', 1)[0] or 'UNCLASSIFIED'

        # Stable identities and connected notes surface first. The original
        # source order provides a deterministic tie breaker without creating
        # any implied importance or institutional ranking.
        ranked = sorted(enumerate(nodes), key=lambda item: (
            item[1].get('identity_stability') != 'stable',
            item[1].get('node_id') not in linked,
            item[1].get('status') not in ('active', 'ratified'),
            item[0],
        ))
        selected = [node for _, node in ranked[:limit]]
        selected_ids = {node.get('node_id') for node in selected}
        projected = []
        for node in selected:
            findings = node.get('validation_findings') or []
            projected.append({
                'id': node.get('node_id'),
                'title': node.get('title') or Path(node.get('source_path', '')).stem,
                'path': node.get('source_path'),
                'category': category(node),
                'type': node.get('node_type', 'unknown'),
                'status': node.get('status') or 'unclassified',
                'owner': node.get('canonical_owner') or node.get('institutional_owner') or 'Unspecified',
                'identity_stability': node.get('identity_stability', 'provisional'),
                'finding_count': len(findings),
                'tags': (node.get('tags') or [])[:6],
            })
        projected_links = [{
            'id': rel.get('relationship_id'), 'type': rel.get('relationship_type'),
            'source': rel.get('source_node_id'), 'target': rel.get('target_node_id'),
            'status': rel.get('status'), 'confidence': rel.get('confidence'),
        } for rel in links if rel.get('source_node_id') in selected_ids and rel.get('target_node_id') in selected_ids]
        categories = {}
        for node in projected:
            categories[node['category']] = categories.get(node['category'], 0) + 1
        return {
            'schema_version': 'council-virtual-brain.v1',
            'mode': 'derived_read_only',
            'authority': 'visual memory projection only; canonical knowledge remains in the Obsidian Vault',
            'source': {
                'kind': 'truth_kernel_projection',
                'coverage_complete': bool(view.get('knowledge_complete', True)),
                'unavailable_count': len(view.get('unavailable_notes', [])),
                'full_node_count': len(nodes), 'full_relationship_count': len(links),
            },
            'truncated': len(nodes) > len(projected),
            'nodes': projected,
            'links': projected_links,
            'categories': [{'id': key, 'count': value} for key, value in sorted(categories.items())],
            'workspace': {'mode': 'not_enabled', 'message': 'No separate memory vault is created here. Capture remains explicit and sourced.'},
        }

    def read(self, relative):
        path = self.root / relative
        resolved = path.resolve()
        if not resolved.is_relative_to(self.root) or resolved.suffix.lower() != '.md':
            raise ValueError('Document non autorisé.')
        if any(part.startswith('.') for part in Path(relative).parts):
            raise ValueError('Document non autorisé.')
        # Only indexed notes, or a newly authored capture, can be requested.
        indexed = self.view and (any(e['path'] == relative for e in self.view['know']['entries']) or relative in self.view.get('unavailable_notes', []))
        captured = resolved.parent == (self.root / CAPTURE_DIR).resolve() and re.fullmatch(r'Capture-[a-f0-9]{32}\.md', resolved.name)
        if not indexed and not captured:
            raise ValueError('Document absent de la mémoire.')
        if getattr(resolved.stat(), 'st_flags', 0) & 0x40000000:
            raise ValueError('Ce document est dans iCloud. Télécharge-le sur le Mac pour le consulter ici.')
        text = resolved.read_text(encoding='utf-8')
        _, metadata, body, _ = alpha_app.vault_validator.parse_frontmatter(text)
        return {'path': relative, 'text': text, 'body': body, 'kind': metadata.get('capture_kind'),
                'status': metadata.get('status'), 'version': hashlib.sha256(text.encode()).hexdigest()}

    def update(self, payload):
        """Explicit author edits, restricted to notes created by this capture flow.

        The supplied content hash rejects stale browser edits. One shared server
        serializes UI writes; external Obsidian edits are checked before publish.
        """
        if not isinstance(payload, dict):
            raise ValueError('Objet JSON attendu.')
        relative = payload.get('path', '')
        if not isinstance(relative, str) or not re.fullmatch(r'14_FUTURE/Founder Ideas/Capture-[a-f0-9]{32}\.md', relative):
            raise ValueError('Seules les saisies créées ici sont modifiables.')
        status, body = payload.get('status'), payload.get('body')
        if status not in ('intake', 'active', 'archived') or not isinstance(body, str) or not 1 <= len(body.strip()) <= 22000:
            raise ValueError('Statut ou contenu invalide.')
        path = self.root / relative
        with self.capture_lock:
            current = self.read(relative)
            if current['version'] != payload.get('version'):
                raise ValueError('Ce document a changé. Rouvre-le avant de le modifier.')
            if current['kind'] not in ('project', 'task') or path.is_symlink():
                raise ValueError('Ce document ne possède pas de suivi de projet.')
            front = current['text'].split('\n---\n', 1)[0]
            front = re.sub(r'^status:.*$', 'status: ' + json.dumps(status), front, flags=re.M)
            front = re.sub(r'^updated:.*$', 'updated: ' + json.dumps(alpha_app.now_iso()), front, flags=re.M)
            content = front + '\n---\n\n' + body.strip() + '\n'
            fd, temporary = tempfile.mkstemp(prefix='.project-', dir=path.parent)
            try:
                with os.fdopen(fd, 'w', encoding='utf-8') as stream:
                    stream.write(content)
                    stream.flush()
                    os.fsync(stream.fileno())
                if hashlib.sha256(path.read_bytes()).hexdigest() != current['version']:
                    raise ValueError('Le document a changé pendant la sauvegarde. Rouvre-le.')
                os.replace(temporary, path)
            finally:
                if os.path.exists(temporary):
                    os.unlink(temporary)
            with self.lock:
                self.generation += 1
                self.updated = 0
        return self.read(relative)

    def capture(self, payload):
        if not isinstance(payload, dict):
            raise ValueError('Objet JSON attendu.')
        title, body, kind, request_id = (payload.get(k) for k in ('title', 'body', 'kind', 'request_id'))
        if not isinstance(title, str) or not 1 <= len(title.strip()) <= 160 or '\n' in title or '\r' in title:
            raise ValueError('Le titre doit contenir de 1 à 160 caractères sur une ligne.')
        if not isinstance(body, str) or not 1 <= len(body.strip()) <= 20000:
            raise ValueError('Le contenu doit contenir de 1 à 20 000 caractères.')
        if kind not in ('note', 'idea', 'task', 'project'):
            raise ValueError('Type de capture inconnu.')
        if not isinstance(request_id, str) or not re.fullmatch(r'[a-f0-9]{32}', request_id):
            raise ValueError('Identifiant de saisie invalide.')
        title, body = title.strip(), body.strip()
        fingerprint = hashlib.sha256(json.dumps([title, body, kind], ensure_ascii=False).encode()).hexdigest()
        directory = self.root / CAPTURE_DIR
        directory.mkdir(parents=True, exist_ok=True)
        if directory.resolve() != directory or not directory.resolve().is_relative_to(self.root):
            raise ValueError('Le dossier de saisie doit être dans le Vault.')
        path = directory / ('Capture-' + request_id + '.md')
        now = alpha_app.now_iso()
        metadata = {
            'title': title, 'aliases': [], 'tags': ['founder-capture', kind],
            'created': now, 'updated': now, 'status': 'intake', 'version': '1.0.0',
            'authors': ['Founder'], 'artifact_type': 'founder_idea',
            'institutional_owner': 'Founder', 'dependencies': [], 'related_documents': [],
            'related_research_programs': [], 'capture_kind': kind, 'capture_fingerprint': fingerprint,
        }
        text = '---\n' + '\n'.join(k + ': ' + json.dumps(v, ensure_ascii=False) for k, v in metadata.items()) + '\n---\n\n# ' + title + '\n\n' + body + '\n'
        with self.capture_lock:
            if path.exists():
                if path.is_symlink() or ('capture_fingerprint: "' + fingerprint + '"') not in path.read_text(encoding='utf-8').split('\n---', 1)[0]:
                    raise ValueError('Cette saisie existe avec un autre contenu. Recommence une nouvelle saisie.')
            else:
                fd, temporary = tempfile.mkstemp(prefix='.capture-', dir=directory)
                try:
                    with os.fdopen(fd, 'w', encoding='utf-8') as stream:
                        stream.write(text)
                        stream.flush()
                        os.fsync(stream.fileno())
                    # Atomic, no-clobber publication; duplicate retries cannot overwrite.
                    os.link(temporary, path)
                finally:
                    os.unlink(temporary)
            with self.lock:
                self.generation += 1
                self.updated = 0
                # Include the saved note immediately while the full derived view refreshes.
                if self.view:
                    note = alpha_app.vault_validator.Note(path, path.relative_to(self.root).as_posix(), text, body, metadata, [], True)
                    entry = alpha_app.index_entry(note, self.root)
                    entry.update(backlinks=0, unresolved=[])
                    entries = [entry] + [e for e in self.view['know']['entries'] if e['path'] != entry['path']]
                    self.view = {**self.view, 'know': {**self.view['know'], 'entries': entries, 'note_count': len(entries)}}
        return {'path': path.relative_to(self.root).as_posix(), 'title': title, 'status': 'intake', 'saved': True}


def make_server(memory, host, port, token=None, universe=None):
    alpha_app.check_reachability_gate(host, port, token)
    csrf = secrets.token_urlsafe(32)
    universe = Path(universe or APP / 'universe/dist/client').resolve()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass  # URLs may contain the existing access credential.

        def send(self, data, status=200, content_type='application/json; charset=utf-8'):
            if not isinstance(data, bytes):
                data = json.dumps(data, ensure_ascii=False).encode()
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Referrer-Policy', 'no-referrer')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('X-Frame-Options', 'SAMEORIGIN')
            self.end_headers()
            try:
                self.wfile.write(data)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def authorized(self, query):
            allowed_hosts = {host}
            if host == '127.0.0.1':
                allowed_hosts.add('localhost')
            if urlsplit('//' + self.headers.get('Host', '')).hostname not in allowed_hosts:
                return False
            if token is None:
                return True
            bearer = self.headers.get('Authorization', '').removeprefix('Bearer ')
            cookie = dict(part.strip().split('=', 1) for part in self.headers.get('Cookie', '').split(';') if '=' in part)
            presented = bearer or query.get('token', [''])[0] or cookie.get('alpha_access', '')
            return hmac.compare_digest(presented, token)

        def do_GET(self):
            parsed = urlsplit(self.path)
            query = parse_qs(parsed.query)
            if not self.authorized(query):
                return self.send({'error': 'Accès privé. Ouvre ton lien personnel Alpha Proxima.'}, 401)
            # Exchange the existing URL token for an HttpOnly session cookie.
            if token and query.get('token'):
                self.send_response(303)
                self.send_header('Set-Cookie', 'alpha_access=' + token + '; HttpOnly; SameSite=Strict; Path=/; Max-Age=604800')
                self.send_header('Location', parsed.path + ('#council' if parsed.path == '/galaxy' else ''))
                self.send_header('Referrer-Policy', 'no-referrer')
                self.send_header('Content-Length', '0')
                self.end_headers()
                return
            route = parsed.path
            try:
                if route in ('/', '/index.html', '/app.html', '/galaxy'):
                    return self.send((APP / 'app/unified.html').read_bytes(), content_type='text/html; charset=utf-8')
                if route == '/api/session':
                    return self.send({'csrf': csrf, 'vault': str(memory.root), 'service':'alpha-proxima-unified', 'code_root':str(APP.parents[1])})
                if route in ('/api/v1/app', '/alpha-api/v1/app', '/api/app'):
                    return self.send(memory.get())
                if route == '/api/v1/system-backbone':
                    return self.send(memory.get()['system_backbone'])
                if route in ('/api/v1/nodes', '/alpha-api/v1/nodes', '/api/v1/truth-kernel', '/api/v1/relationships', '/api/v1/validation', '/api/v1/health'):
                    memory.get()
                    contract = memory.contract
                    if contract is None:
                        raise NotReady('Lecture du Vault en cours.')
                    if route.endswith('/nodes'):
                        return self.send({'schema_version': '1.0.0', 'nodes': contract['nodes']})
                    if route.endswith('/relationships'):
                        return self.send({key: contract[key] for key in ('schema_version','relationships','unresolved_relationships')})
                    if route.endswith('/validation'):
                        return self.send(contract['validation'])
                    if route.endswith('/health'):
                        return self.send(alpha_app.truth_kernel.summary(contract))
                    return self.send(contract)
                if route == '/api/state':
                    return self.send({'error': 'Raw state retired', 'replacement': '/api/v1/app'}, 410)
                if route == '/api/note':
                    return self.send(memory.read(query.get('path', [''])[0]))
                if route == '/classic':
                    return self.send(alpha_app.render_app(memory.get(), alpha_app.DEFAULT_TEMPLATE).encode(), content_type='text/html; charset=utf-8')
                if route == '/council-view':
                    view = galaxy.build_galaxy_view(memory.root, brain=memory.brain())
                    return self.send(galaxy.render_app(view, galaxy.DEFAULT_TEMPLATE).encode(), content_type='text/html; charset=utf-8')
                if route == '/office':
                    return self.send(office_spatial.render_app(office_spatial.build_office_view(memory.root, brain=memory.brain()), office_spatial.DEFAULT_TEMPLATE).encode(), content_type='text/html; charset=utf-8')
                if route == '/api/galaxy':
                    return self.send(galaxy.build_galaxy_view(memory.root, brain=memory.brain()))
                if route == '/api/office':
                    return self.send(office_spatial.build_office_view(memory.root, brain=memory.brain()))
                if route.startswith('/universe/'):
                    relative = unquote(route[len('/universe/'):]) or 'index.html'
                    path = (universe / relative).resolve()
                    if not path.is_relative_to(universe) or not path.is_file():
                        return self.send({'error': 'Not found'}, 404)
                    return self.send(path.read_bytes(), content_type=mimetypes.guess_type(path.name)[0] or 'application/octet-stream')
                return self.send({'error': 'Not found'}, 404)
            except NotReady as exc:
                self.send({'error': str(exc), 'loading': True}, 503)
            except (ValueError, OSError, RuntimeError) as exc:
                self.send({'error': str(exc)}, 400)

        def do_POST(self):
            parsed = urlsplit(self.path)
            if not self.authorized(parse_qs(parsed.query)):
                return self.send({'error': 'Unauthorized'}, 401)
            if parsed.path not in ('/api/capture', '/api/project/update'):
                return self.send({'error': 'Not found'}, 404)
            if not hmac.compare_digest(self.headers.get('X-Alpha-CSRF', ''), csrf):
                return self.send({'error': 'Recharge la page avant de sauvegarder.'}, 403)
            origin = self.headers.get('Origin')
            if origin and urlsplit(origin).netloc != self.headers.get('Host'):
                return self.send({'error': 'Origin refused'}, 403)
            if self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
                return self.send({'error': 'JSON required'}, 415)
            try:
                size = int(self.headers.get('Content-Length', '0'))
                if not 1 <= size <= 100000:
                    return self.send({'error': 'Saisie trop volumineuse.'}, 413)
                self.connection.settimeout(15)
                payload = json.loads(self.rfile.read(size))
                result = memory.capture(payload) if parsed.path == '/api/capture' else memory.update(payload)
                self.send(result, 201)
            except (ValueError, OSError) as exc:
                self.send({'error': str(exc)}, 400)

    return ThreadingHTTPServer((host, port), Handler)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8788)
    parser.add_argument('--remote-config', help='Existing private host/port/token JSON; no credentials on the command line.')
    parser.add_argument('--redirect-port', type=int, help='Loopback redirect for the former standalone prototype.')
    args = parser.parse_args()
    memory = Memory(args.root)
    memory.refresh()
    server = make_server(memory, args.host, args.port, os.environ.get('ALPHA_APP_TOKEN'))
    if args.remote_config:
        config = json.loads(Path(args.remote_config).read_text())
        remote = make_server(memory, config['host'], config['port'], config['token'])
        threading.Thread(target=remote.serve_forever, daemon=True).start()
    if args.redirect_port:
        class Redirect(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass
            def do_GET(self):
                self.send_response(302)
                self.send_header('Location', 'http://127.0.0.1:' + str(args.port) + '/#universe')
                self.send_header('Content-Length', '0')
                self.end_headers()
        redirect = ThreadingHTTPServer(('127.0.0.1', args.redirect_port), Redirect)
        threading.Thread(target=redirect.serve_forever, daemon=True).start()
    server.serve_forever()


if __name__ == '__main__':
    main()
