import { useEffect, useRef, useState } from 'react'
import {baseSystems} from './systems.js'
import SpatialScene from './SpatialScene.jsx'
import DepartmentWorkspace from './DepartmentWorkspace.jsx'
import './styles.css'

// The seven points are a presentation map for the auric body. They are deliberately
// separate from institutional authority: a Vault note becomes a system objective only
// when its owner is explicit, while every note remains discoverable in the thought cloud.

const pathLabels = ['Founder Intent', 'Route Plan', 'Context', 'Specialist Run', 'Result', 'Synthesis', 'Memory']

const QUIET_DELAY = 3800

export function App() {
  const [workspaceOpen, setWorkspaceOpen] = useState(false)
  const [viewRequest, setViewRequest] = useState({view:'front',sequence:0})
  const [mode, setMode] = useState('orbit')
  const [embodiment, setEmbodiment] = useState('organic')
  const [selected, setSelected] = useState('LUMIAION')
  const [panelOpen, setPanelOpen] = useState(false)
  const [quiet, setQuiet] = useState(false)
  const [vault, setVault] = useState(null)
  const [kernel, setKernel] = useState(null)
  const [vaultError, setVaultError] = useState('')
  const [focusedObjective, setFocusedObjective] = useState(null)
  const [command, setCommand] = useState('')
  const [commandFeedback, setCommandFeedback] = useState('Rechercher dans ta mémoire')
  const systems = baseSystems.map((system) => {
    const department = kernel?.departments?.find((item) => item.id === system.id)
    const fallback = vault?.departments?.find((item) => item.id === system.id)
    return { ...system, status: department ? `${department.nodeCount} notes · ${department.attentionCount} signaux` : fallback ? `${fallback.attentionCount} attention` : 'Awaiting Vault', objectives: department?.objectives || fallback?.objectives || [] }
  })
  const active = systems.find((system) => system.id === selected) || systems[0]
  const primaryAttention = vault?.attention?.[0]
  const objective = focusedObjective || active.objectives[0] || primaryAttention
  const nodes = kernel?.nodes || []
  const pathSteps = [
    { title: 'Founder Intent', detail: objective?.title || 'Select an objective' },
    { title: 'Route Plan', detail: active.name },
    { title: 'Context', detail: objective ? `${objective.status || 'à consulter'} · ${objective.nodeType || objective.kind || 'signal'}` : 'No active context' },
    { title: 'Specialist Run', detail: `${active.name} control center` },
    { title: 'Result', detail: objective ? `${objective.relationshipCount ?? 0} relations · ${objective.unresolvedCount ?? 0} unresolved` : 'Awaiting work' },
    { title: 'Synthesis', detail: objective?.owner || objective?.excerpt || active.detail },
    { title: 'Memory', detail: objective?.path || 'Obsidian Vault' },
  ]
  function choose(id) { setSelected(id); setFocusedObjective(null); setPanelOpen(true); setMode('surface') }
  function openSourceNote(path, title) {
    if (!path) return
    if (window.parent !== window) window.parent.postMessage({ type: 'open-note', path, title }, location.origin)
    else window.location.href = `${import.meta.env.DEV ? 'http://127.0.0.1:8788' : location.origin}/#document?path=${encodeURIComponent(path)}&title=${encodeURIComponent(title || path)}`
  }
  function openCenterMemory(center) {
    if (window.parent !== window) window.parent.postMessage({type:'open-center', center}, location.origin)
    else window.location.href = `${import.meta.env.DEV ? 'http://127.0.0.1:8788' : location.origin}/#memory?search=${encodeURIComponent(center)}`
  }
  function routeCommand(event) {
    event.preventDefault()
    const query = command.trim().toLowerCase()
    if (!query) return
    const matchedObjective = kernel?.nodes?.find((item) => `${item.title} ${item.path} ${item.nodeType} ${item.owner || ''} ${item.department}`.toLowerCase().includes(query))
      || vault?.attention?.find((item) => `${item.title} ${item.excerpt} ${item.status} ${item.department}`.toLowerCase().includes(query))
    const matchedDepartment = systems.find((system) => `${system.id} ${system.center} ${system.detail}`.toLowerCase().includes(query))
    if (matchedObjective) {
      setSelected(matchedObjective.department || 'LUMIAION')
      setFocusedObjective(matchedObjective)
      setPanelOpen(true)
      setMode('surface')
      setCommandFeedback(matchedObjective.department ? `Centre ${matchedObjective.department}` : 'Note retrouvée')
    } else if (matchedDepartment) {
      choose(matchedDepartment.id)
      setCommandFeedback(`Entered ${matchedDepartment.id}`)
    } else {
      setCommandFeedback('No matching Vault signal — try governance, research, health, finance, or consciousness')
    }
    setCommand('')
  }

  useEffect(() => {
    let activeRequest = true
    let pending = false
    let controller
    async function loadUnifiedModel() {
      if(pending || !activeRequest) return
      pending = true
      controller = new AbortController()
      const timeout = setTimeout(() => controller.abort(), 15000)
      try {
        const appResponse = await fetch('/api/v1/app', {cache:'no-store', signal:controller.signal})
        const data = await appResponse.json()
        if (!appResponse.ok) throw new Error(data.error || 'Mémoire indisponible')
        const backbone = data.system_backbone || {}
        const names = new Set(baseSystems.map(s => s.id))
        // Only explicit owner matches route institutional signals to a center.
        // Unassigned knowledge remains available in the common Memory view.
        const departmentFor = owner => names.has(owner) ? owner : null
        const nodes = (data.know?.entries || []).map(entry => ({
          ...entry, nodeType:entry.type, department:departmentFor(entry.owner),
          relationshipCount:entry.links?.length || 0, unresolvedCount:entry.unresolved?.length || 0,
          openActions:0,
        }))
        const attention = (backbone.attention || []).map(item => ({
          ...item, department:departmentFor(item.owner), status:item.severity || 'à consulter',
        }))
        const departments = baseSystems.map(system => {
          const records=nodes.filter(n=>n.department===system.id)
          const signals=attention.filter(n=>n.department===system.id)
          return {id:system.id,nodeCount:records.length,attentionCount:signals.length,objectives:[...signals,...records].slice(0,12)}
        })
        if (activeRequest) {
          setVault({source:data.source?.vault || 'Obsidian Vault',readOnly:true,noteCount:data.know?.note_count || 0,attentionCount:attention.length,departments,attention})
          setKernel({departments,nodes,counts:{nodes:data.know?.note_count || 0}})
          setVaultError('')
        }
      } catch (error) {
        if (activeRequest) setVaultError(error.name === "AbortError" ? "Lecture trop longue. Nouvelle tentative bientôt." : error.message)
      } finally { clearTimeout(timeout); pending = false }
    }
    loadUnifiedModel()
    const modelInterval = setInterval(loadUnifiedModel, 10000)
    const onMemory = event => { if(event.origin === location.origin && event.data?.type === 'memory-updated') loadUnifiedModel() }
    window.addEventListener('message',onMemory)
    return () => { activeRequest = false; controller?.abort(); clearInterval(modelInterval); window.removeEventListener('message',onMemory) }
  }, [])

  useEffect(() => {
    let timer
    function wake() {
      setQuiet(false)
      clearTimeout(timer)
      timer = setTimeout(() => setQuiet(true), QUIET_DELAY)
    }
    wake()
    const events = ['pointermove', 'pointerdown', 'keydown', 'wheel']
    events.forEach((event) => window.addEventListener(event, wake, { passive: true }))
    return () => {
      clearTimeout(timer)
      events.forEach((event) => window.removeEventListener(event, wake))
    }
  }, [])

  return <main className={`app mode-${mode}${quiet ? ' quiet' : ''}`}>

    <SpatialScene mode={mode} viewRequest={viewRequest} embodiment={embodiment} selected={selected} onSelect={choose} onOpenNote={openSourceNote} systems={systems} nodes={nodes} />
    <div className="atmosphere" />
    <nav className="perspectives glass" aria-label="Points de vue du corps">
      <button onClick={() => {setMode('orbit');setPanelOpen(false);setViewRequest(v=>({view:'front',sequence:v.sequence+1}))}}>Face</button>
      <button onClick={() => {setMode('orbit');setPanelOpen(false);setViewRequest(v=>({view:'side',sequence:v.sequence+1}))}}>Profil</button>
      <button onClick={() => {setMode('orbit');setPanelOpen(false);setViewRequest(v=>({view:'back',sequence:v.sequence+1}))}}>Dos</button>
      <button onClick={() => {setMode('inward');setPanelOpen(false)}}>À l’intérieur</button>
    </nav>
    {workspaceOpen && <DepartmentWorkspace system={active} nodes={nodes.filter(n=>n.department===active.id)} onClose={()=>setWorkspaceOpen(false)} onOpenNote={openSourceNote} onOpenCenter={openCenterMemory} />}
    {mode !== 'orbit' && <button className="open-workspace" style={{'--center-color':'#'+active.color.toString(16).padStart(6,'0')}} onClick={()=>setWorkspaceOpen(true)}>Travailler avec {active.name}</button>}
    <nav className="embodiment glass" aria-label="Visualisation du vivant">
      <button aria-pressed={embodiment === 'organic'} onClick={() => setEmbodiment('organic')}>Corps vivant</button>
      <button aria-pressed={embodiment === 'neural'} onClick={() => setEmbodiment('neural')}>Réseau cosmique</button>
    </nav>
    <header><div className="brand"><span>ALPHA PROXIMA</span><strong>FOUNDER OS</strong><small>LUMIAION CONSCIOUSNESS FIELD</small></div><div className="view-title"><span>ORBITAL KNOWLEDGE FIELD</span><small>Observe the whole. Enter what needs attention.</small></div><div className={`truth ${vaultError ? 'offline' : ''}`}><i /> {kernel ? 'MÉMOIRE CONNECTÉE' : vaultError ? 'MÉMOIRE INDISPONIBLE' : 'LECTURE DU VAULT'} <small>{kernel ? `${kernel.counts.nodes} NOTES · OBSERVER` : 'TON ESPACE'}</small></div></header>
    <aside className="mission glass"><p className="eyebrow">FOUNDER ATTENTION</p><h2>{primaryAttention?.title || (vaultError ? 'Mémoire en attente' : 'Lecture de ta mémoire…')}</h2><div className="rule"/><p className="eyebrow">ORIENTATION</p><p>{primaryAttention ? `${primaryAttention.department || primaryAttention.owner || 'Founder'} · ${primaryAttention.status}` : vaultError || 'Reading the Vault without changing it.'}</p>{primaryAttention && <button onClick={() => { setSelected(primaryAttention.department || 'LUMIAION'); setFocusedObjective(primaryAttention); setPanelOpen(true); setMode('surface') }}>ENTER PRIORITY</button>}<div className="health"><p className="eyebrow">MEMORY FIELD</p><span>Markdown notes <b>{vault?.noteCount ?? '—'}</b></span><span>Need attention <b>{vault?.attentionCount ?? '—'}</b></span><span>Authority <b>Observer</b></span></div></aside>
    {mode !== 'inward' && <div className="beacon-index" aria-label="Department chakra control centers">{systems.map((system) => <button key={system.id} style={{'--center-color':'#'+system.color.toString(16).padStart(6,'0')}} className={selected === system.id ? 'active' : ''} onClick={() => choose(system.id)}><span>{system.name}</span><small>{system.center} · {system.status}</small></button>)}</div>}
    {mode === 'inward' && <div className="inside-caption"><span>À L’INTÉRIEUR DU MÊME CORPS</span><b>{active.name} · {active.center}</b><small>Glisse pour regarder autour de toi. Dézoome pour ressortir.</small></div>}
    {panelOpen && <aside className="inspector glass"><button className="close" onClick={() => setPanelOpen(false)} aria-label="Close inspector">×</button><p className="eyebrow">{active.center} · {active.chakra}</p><h2>{focusedObjective?.title || active.name}</h2><p className="status">{focusedObjective?.status || active.status}</p><div className="rule"/><p className="eyebrow">{active.name} OPERATING FIELD</p><p>{focusedObjective?.path || active.detail}</p>{!focusedObjective && active.objectives.length > 0 && <div className="objective-list">{active.objectives.slice(0, 3).map((item) => <button key={item.id} className={objective?.id === item.id ? 'active' : ''} onClick={() => setFocusedObjective(item)}><span>{item.title}</span><small>{item.status}{item.nodeType ? ` · ${item.nodeType.replaceAll('_', ' ')}` : item.inferred ? ' · inferred route' : ''}</small></button>)}</div>}<div className="signal"><span>{objective?.nodeType ? 'Kernel provenance' : 'Memory source'}</span><b>{objective?.path ? 'Vault' : '—'}</b></div><button className="field-button" onClick={() => openCenterMemory(active.name)}>OPEN {active.name} MEMORY FIELD</button><button onClick={() => setMode(mode === 'surface' ? 'inward' : 'surface')}>{mode === 'surface' ? 'DIVE INTO KNOWLEDGE' : 'ENTER CENTER'}</button></aside>}
    {objective?.path && mode !== 'orbit' && <button className="source-link" onClick={() => openSourceNote(objective.path, objective.title)}>Lire la note source ↗</button>}
    <div className="depth-readout"><span>ENVIRONMENT</span><b>{mode === 'orbit' ? '01 / ORBITAL FIELD' : mode === 'surface' ? '02 / SYSTEM SURFACE' : '03 / KNOWLEDGE CORE'}</b></div>
    <p className="gesture-hint">{mode === 'orbit' ? 'ROTATION LIBRE · ZOOM · CHOISIS UN CENTRE' : mode === 'surface' ? 'CLOSE INSPECTION · SELECT ANOTHER SYSTEM' : 'REGARDE DE L’INTÉRIEUR VERS L’EXTÉRIEUR'}</p>
    <div className="cloud-status glass"><span>THOUGHT CLOUD</span><b>{nodes.length} VAULT NODES</b><small>Touch a point to open its source note</small></div>
    <nav className="modes glass" aria-label="Spatial view"><button className={mode === 'orbit' ? 'active' : ''} onClick={() => setMode('orbit')}><i>01</i><span>ORBIT</span></button><button className={mode === 'surface' ? 'active' : ''} onClick={() => setMode('surface')}><i>02</i><span>SURFACE</span></button><button className={mode === 'inward' ? 'active' : ''} onClick={() => setMode('inward')}><i>03</i><span>INWARD</span></button></nav>
    <form className="command glass" onSubmit={routeCommand}><label htmlFor="directive">MÉMOIRE · {commandFeedback}</label><input id="directive" value={command} onChange={(event) => setCommand(event.target.value)} placeholder="Un titre, un domaine…"/><button>CHERCHER</button></form>
  </main>
}
