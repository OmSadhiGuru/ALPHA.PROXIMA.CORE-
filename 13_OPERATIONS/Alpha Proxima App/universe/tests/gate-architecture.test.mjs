import test from 'node:test'
import assert from 'node:assert/strict'
import {readFile} from 'node:fs/promises'
import {fileURLToPath} from 'node:url'
import path from 'node:path'

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
const read=relative=>readFile(path.join(root,relative),'utf8')

test('the approved energetic being remains the single visual body',async()=>{
  const app=await read('src/App.jsx')
  const scene=await read('src/SpatialScene.jsx')
  const volume=await read('src/body-volume.js')
  assert.match(app,/className="gate-art"/)
  assert.match(app,/alpha-hero-gold-v2\.jpg/)
  assert.doesNotMatch(scene,/athletic-human|auric-human|higgsfield-botanical|GLTFLoader/)
  assert.doesNotMatch(app,/Corps vivant|Réseau cosmique|ORBIT|SURFACE|INWARD/)
  assert.match(scene,/makeVolumetricBeing/)
  assert.match(scene,/bodyPivot\.rotation\.y/)
  assert.match(scene,/uFlatVisibility/)
  assert.match(volume,/yawLimit:Math\.PI/)
  assert.match(volume,/depthScale:\.38/)
  assert.match(scene,/createBodyGeometry/)
})

test('seven accessible vortex portals lead to department hubs',async()=>{
  const systems=await read('src/systems.js')
  const app=await read('src/App.jsx')
  const workspace=await read('src/DepartmentWorkspace.jsx')
  assert.equal((systems.match(/anchor:\[/g)||[]).length,7)
  assert.match(app,/aria-label="Portails des départements"/)
  assert.match(app,/phase==='portal'/)
  assert.match(app,/phase==='hub'/)
  assert.match(workspace,/role="dialog"/)
  assert.match(workspace,/aria-modal="true"/)
  assert.match(workspace,/role="tablist"/)
})

test('reduced motion and WebGL fallback preserve navigation',async()=>{
  const app=await read('src/App.jsx')
  const scene=await read('src/SpatialScene.jsx')
  const styles=await read('src/styles.css')
  assert.match(app,/query\.has\('reduced-motion'\)/)
  assert.match(app,/query\.has\('fallback'\)/)
  assert.match(scene,/forceFallback/)
  assert.match(styles,/@media\(prefers-reduced-motion:reduce\)/)
  assert.match(styles,/\.webgl-fallback/)
})

test('the parent shell keeps the Universe mounted across routes',async()=>{
  const shell=await read('../app/unified.html')
  const route=shell.match(/function route\(\)\{[^}]+(?:\}[^}]*)*\}/)?.[0]||shell
  assert.match(shell,/universeFrame\.inert=!universeActive/)
  assert.match(shell,/type:'universe-visibility'/)
  assert.doesNotMatch(route,/universe-frame'\)\.removeAttribute\('src'/)
})
