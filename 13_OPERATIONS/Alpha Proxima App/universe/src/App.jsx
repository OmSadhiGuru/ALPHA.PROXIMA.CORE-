import {useCallback, useEffect, useMemo, useRef, useState} from 'react'
import {baseSystems} from './systems.js'
import {PORTAL_DURATION_MS} from './gate-depth.js'
import SpatialScene from './SpatialScene.jsx'
import DepartmentWorkspace from './DepartmentWorkspace.jsx'
import './styles.css'

const SESSION_KEY = 'alpha-proxima.gate-of-soul.v1'
const IMAGE_SIZE = {width:1586,height:992}

function storedGateState(){
  try{return JSON.parse(sessionStorage.getItem(SESSION_KEY)||'{}')}catch{return {}}
}

function usePortalLayout(systems){
  const [positions,setPositions]=useState({})
  useEffect(()=>{
    let frame=0
    const place=()=>{
      cancelAnimationFrame(frame)
      frame=requestAnimationFrame(()=>{
        const width=window.innerWidth,height=window.innerHeight
        const scale=Math.max(width/IMAGE_SIZE.width,height/IMAGE_SIZE.height)
        const renderedWidth=IMAGE_SIZE.width*scale,renderedHeight=IMAGE_SIZE.height*scale
        const objectX=width<=720?.61:.5
        const offsetX=(width-renderedWidth)*objectX
        const offsetY=(height-renderedHeight)*.5
        setPositions(Object.fromEntries(systems.map(system=>[system.id,{left:offsetX+system.anchor[0]*renderedWidth,top:offsetY+system.anchor[1]*renderedHeight}])))
      })
    }
    place();window.addEventListener('resize',place)
    return()=>{cancelAnimationFrame(frame);window.removeEventListener('resize',place)}
  },[systems])
  return positions
}

export function App(){
  const restored=useMemo(storedGateState,[])
  const query=useMemo(()=>new URLSearchParams(location.search),[])
  const [mediaReduced,setMediaReduced]=useState(()=>window.matchMedia('(prefers-reduced-motion: reduce)').matches)
  const reducedMotion=mediaReduced||query.has('reduced-motion')
  const forceFallback=query.has('fallback')
  const [phase,setPhase]=useState(restored.entered?'gate':'arrival')
  const [selected,setSelected]=useState(restored.selected||'LUMIAION')
  const [portalSequence,setPortalSequence]=useState(0)
  const [paused,setPaused]=useState(reducedMotion)
  const [routeVisible,setRouteVisible]=useState(true)
  const [documentVisible,setDocumentVisible]=useState(()=>!document.hidden)
  const [webglFallback,setWebglFallback]=useState(forceFallback)
  const [spatialReady,setSpatialReady]=useState(false)
  const [depthEnabled,setDepthEnabled]=useState(restored.depthEnabled!==false)
  const [viewResetKey,setViewResetKey]=useState(0)
  const [vault,setVault]=useState(null)
  const [kernel,setKernel]=useState(null)
  const [vaultError,setVaultError]=useState('')
  const [command,setCommand]=useState('')
  const [commandFeedback,setCommandFeedback]=useState('Chercher un titre ou un département')
  const portalTimer=useRef()
  const portalButtons=useRef({})
  const projectedPositions=useRef({})
  const spatialReadyRef=useRef(false)
  const visible=routeVisible&&documentVisible
  const systems=baseSystems.map(system=>{
    const department=kernel?.departments?.find(item=>item.id===system.id)
    return {...system,status:department?`${department.nodeCount} notes · ${department.attentionCount} signaux`:'Aucun signal attribué',objectives:department?.objectives||[]}
  })
  const active=systems.find(system=>system.id===selected)||systems[0]
  const positions=usePortalLayout(baseSystems)
  const nodes=kernel?.nodes||[]

  const placePortalButtons=useCallback(points=>{
    Object.entries(portalButtons.current).forEach(([id,node])=>{
      const point=points[id]
      if(!node||!point)return
      node.style.left=`${point.left}px`
      node.style.top=`${point.top}px`
    })
  },[])

  const onProject=useCallback(points=>{
    projectedPositions.current=points
    if(spatialReadyRef.current)placePortalButtons(points)
  },[placePortalButtons])

  const onSceneReady=useCallback(ready=>{
    spatialReadyRef.current=ready
    setSpatialReady(ready)
    if(ready)placePortalButtons(projectedPositions.current)
  },[placePortalButtons])

  useEffect(()=>{
    if(!spatialReady)placePortalButtons(positions)
  },[positions,spatialReady,phase,placePortalButtons])

  useEffect(()=>{
    try{sessionStorage.setItem(SESSION_KEY,JSON.stringify({entered:phase!=='arrival',selected,depthEnabled}))}catch{}
  },[phase,selected,depthEnabled])

  useEffect(()=>()=>clearTimeout(portalTimer.current),[])

  useEffect(()=>{
    const preference=window.matchMedia('(prefers-reduced-motion: reduce)')
    const update=event=>{setMediaReduced(event.matches);if(event.matches)setPaused(true)}
    preference.addEventListener('change',update)
    return()=>preference.removeEventListener('change',update)
  },[])

  useEffect(()=>{
    const onMessage=event=>{
      if(event.origin!==location.origin)return
      if(event.data?.type==='memory-updated')loadModel()
      if(event.data?.type==='universe-visibility')setRouteVisible(Boolean(event.data.visible))
    }
    window.addEventListener('message',onMessage)
    return()=>window.removeEventListener('message',onMessage)
  })

  useEffect(()=>{
    const onVisibility=()=>setDocumentVisible(!document.hidden)
    document.addEventListener('visibilitychange',onVisibility)
    return()=>document.removeEventListener('visibilitychange',onVisibility)
  },[])

  async function loadModel(){
    try{
      const response=await fetch('/api/v1/app',{cache:'no-store'})
      const data=await response.json()
      if(!response.ok)throw new Error(data.error||'Mémoire indisponible')
      const names=new Set(baseSystems.map(system=>system.id))
      const departmentFor=owner=>names.has(owner)?owner:null
      const entries=(data.know?.entries||[]).map(entry=>({...entry,nodeType:entry.type,department:departmentFor(entry.owner),relationshipCount:entry.links?.length||0,unresolvedCount:entry.unresolved?.length||0}))
      const attention=(data.system_backbone?.attention||[]).map(item=>({...item,department:departmentFor(item.owner),status:item.severity||'à consulter'}))
      const departments=baseSystems.map(system=>{
        const records=entries.filter(item=>item.department===system.id)
        const signals=attention.filter(item=>item.department===system.id)
        return {id:system.id,nodeCount:records.length,attentionCount:signals.length,objectives:[...signals,...records].slice(0,12)}
      })
      setVault({source:data.source?.vault||'Obsidian Vault',noteCount:data.know?.note_count||0,attentionCount:attention.length})
      setKernel({nodes:entries,departments,counts:{nodes:data.know?.note_count||0}})
      setVaultError('')
    }catch(error){setVaultError(error.message)}
  }

  useEffect(()=>{
    if(!visible)return
    loadModel()
    const timer=setInterval(loadModel,10000)
    return()=>clearInterval(timer)
  },[visible])

  function enterGate(){setPhase('gate')}

  function openPortal(id){
    clearTimeout(portalTimer.current)
    setSelected(id);setPhase('portal');setPortalSequence(value=>value+1)
    portalTimer.current=setTimeout(()=>setPhase('hub'),reducedMotion||paused?40:PORTAL_DURATION_MS+60)
  }

  function closeHub(){
    setPhase('gate')
    requestAnimationFrame(()=>portalButtons.current[selected]?.focus())
  }

  function openSourceNote(path,title){
    if(!path)return
    if(window.parent!==window)window.parent.postMessage({type:'open-note',path,title},location.origin)
    else window.location.href=`${import.meta.env.DEV?'http://127.0.0.1:8788':location.origin}/#document?path=${encodeURIComponent(path)}&title=${encodeURIComponent(title||path)}`
  }

  function openCenterMemory(center){
    if(window.parent!==window)window.parent.postMessage({type:'open-center',center},location.origin)
    else window.location.href=`${import.meta.env.DEV?'http://127.0.0.1:8788':location.origin}/#memory?search=${encodeURIComponent(center)}`
  }

  function routeCommand(event){
    event.preventDefault()
    const queryValue=command.trim().toLowerCase()
    if(!queryValue)return
    const department=systems.find(system=>`${system.name} ${system.center} ${system.chakra} ${system.detail}`.toLowerCase().includes(queryValue))
    const node=nodes.find(item=>`${item.title} ${item.path} ${item.owner||''} ${item.department||''}`.toLowerCase().includes(queryValue))
    const target=department?.id||node?.department
    if(target){setCommandFeedback(node?`Note trouvée dans ${target}`:`Portail ${target}`);setCommand('');openPortal(target)}
    else setCommandFeedback('Aucun signal attribué — essaie santé, stratégie, conscience ou recherche')
  }

  const activeColor=`#${active.color.toString(16).padStart(6,'0')}`
  const embedded=window.parent!==window
  const showGate=phase==='gate'||phase==='portal'

  return <main className={`gate-app phase-${phase}${paused?' field-paused':''}${reducedMotion?' motion-reduced':''}${webglFallback?' webgl-fallback':''}${embedded?' embedded':''}${spatialReady?' spatial-ready':''}${depthEnabled?' spatial-enabled':''}`} style={{'--active-color':activeColor}}>
    <img className="gate-art" src={`${import.meta.env.BASE_URL}assets/alpha-hero-gold-v2.jpg`} alt="" aria-hidden="true" fetchPriority="high" decoding="async" />
    <SpatialScene systems={systems} activeId={selected} phase={phase} portalSequence={portalSequence} paused={paused} visible={visible} reducedMotion={reducedMotion} forceFallback={forceFallback} onFallback={setWebglFallback} onProject={onProject} onReady={onSceneReady} depthEnabled={depthEnabled} viewResetKey={viewResetKey}/>
    <div className="gate-vignette" aria-hidden="true"/>

    {phase==='arrival'&&<section className="arrival" aria-labelledby="arrival-title">
      <div className="arrival-copy">
        <p className="kicker">ALPHA PROXIMA · GATE OF THE SOUL</p>
        <h1 id="arrival-title">Un univers pour relier tes idées <em>à l’action.</em></h1>
        <p>Entre par le centre vivant. Chaque chakra ouvre un département, sans quitter le même monde.</p>
        <button className="enter-gate" onClick={enterGate}>Éveiller le portail <span aria-hidden="true">→</span></button>
      </div>
    </section>}

    {showGate&&<>
      <section className="gate-heading" aria-live="polite">
        <p className="kicker">GATE OF THE SOUL</p>
        <h1>{phase==='portal'?`Passage vers ${active.name}`:'Choisis ton centre.'}</h1>
        <p>{phase==='portal'?active.invitation:'Sept vortex. Sept domaines. Un seul espace vivant.'}</p>
      </section>

      <nav className="chakra-portals" aria-label="Portails des départements">
        {systems.map(system=>{
          return <button key={system.id} ref={node=>{
            portalButtons.current[system.id]=node
            const point=(spatialReadyRef.current?projectedPositions.current:positions)[system.id]||positions[system.id]
            if(node&&point){node.style.left=`${point.left}px`;node.style.top=`${point.top}px`}
          }} className={selected===system.id?'selected':''} style={{'--portal-color':`#${system.color.toString(16).padStart(6,'0')}`}} disabled={phase==='portal'} aria-label={`Ouvrir ${system.name}, portail ${system.center}`} aria-current={selected===system.id?'true':undefined} onFocus={()=>phase==='gate'&&setSelected(system.id)} onPointerEnter={()=>phase==='gate'&&setSelected(system.id)} onClick={()=>openPortal(system.id)}>
            <span className="portal-hit" aria-hidden="true"/>
            <span className="portal-label"><b>{system.name}</b><small>{system.center}</small></span>
          </button>
        })}
      </nav>

      <div className="gate-status" role="status">
        <span className="live-dot"/> {webglFallback?'MODE VISUEL ESSENTIEL':paused?'CHAMP FIGÉ':'CHAMP VIVANT'}
        <small>{vaultError?'Mémoire indisponible':kernel?`${kernel.counts.nodes} notes · Observer`:'Lecture du Vault…'}</small>
      </div>
      <button className="pause-field" aria-pressed={paused} disabled={reducedMotion||phase==='portal'} onClick={()=>setPaused(value=>!value)}>{reducedMotion?'Mouvement réduit':paused?'Animer le champ':'Figer le champ'}</button>
      {!webglFallback&&spatialReady&&<aside className="spatial-controls" aria-label="Vue du portail">
        <div className="spatial-actions">
          <div className="spatial-mode" role="group" aria-label="Profondeur de la vue">
            <button type="button" aria-pressed={!depthEnabled} disabled={phase==='portal'} onClick={()=>setDepthEnabled(false)}>2D</button>
            <button type="button" aria-pressed={depthEnabled} disabled={phase==='portal'} onClick={()=>setDepthEnabled(true)}>3D</button>
          </div>
          <button type="button" className="recenter-view" disabled={phase==='portal'||!depthEnabled} onClick={()=>setViewResetKey(value=>value+1)} aria-label="Recentrer la vue du portail">Recentrer</button>
        </div>
        <p className="spatial-hint">{depthEnabled?'Glisse pour explorer':'L’image, au repos'}</p>
      </aside>}
      <form className="gate-search" onSubmit={routeCommand}>
        <label htmlFor="gate-command">Mémoire · {commandFeedback}</label>
        <div><input id="gate-command" value={command} onChange={event=>setCommand(event.target.value)} placeholder="Un titre, un domaine…"/><button>Entrer</button></div>
      </form>
    </>}

    {phase==='hub'&&<DepartmentWorkspace system={active} systems={systems} nodes={nodes.filter(node=>node.department===active.id)} vault={vault} onClose={closeHub} onSwitch={openPortal} onOpenNote={openSourceNote} onOpenCenter={openCenterMemory}/>}
  </main>
}
