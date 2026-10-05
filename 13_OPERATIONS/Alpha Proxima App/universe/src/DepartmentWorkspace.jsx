import {useEffect,useRef,useState} from 'react'

const SHORTCUT_KEY='alpha-proxima.department-shortcuts.v1'
const TABS=['Portal','Mémoire','Outils']

function loadShortcuts(){try{return JSON.parse(localStorage.getItem(SHORTCUT_KEY)||'{}')}catch{return {}}}

export default function DepartmentWorkspace({system,systems,nodes,vault,onClose,onSwitch,onOpenNote,onOpenCenter}){
  const dialogRef=useRef(null)
  const tabRefs=useRef([])
  const [tab,setTab]=useState('Portal')
  const [links,setLinks]=useState(loadShortcuts)
  const [name,setName]=useState('')
  const [url,setUrl]=useState('')
  const [kind,setKind]=useState('Outil')
  const [error,setError]=useState('')
  const rows=links[system.id]||[]
  const color=`#${system.color.toString(16).padStart(6,'0')}`

  useEffect(()=>{dialogRef.current?.querySelector('.hub-back')?.focus()},[])

  function save(event){
    event.preventDefault();setError('')
    let parsed
    try{parsed=new URL(url);if(!['https:','http:'].includes(parsed.protocol)||parsed.username||parsed.password)throw new Error()}
    catch{setError('Utilise une adresse web http ou https, sans identifiant ni mot de passe.');return}
    if(!name.trim())return
    const next={...links,[system.id]:[...rows,{id:crypto.randomUUID(),name:name.trim(),url:parsed.href,kind}]}
    try{localStorage.setItem(SHORTCUT_KEY,JSON.stringify(next));setLinks(next);setName('');setUrl('')}
    catch{setError('Impossible d’enregistrer ce raccourci dans ce navigateur.')}
  }

  function remove(id){
    const next={...links,[system.id]:rows.filter(row=>row.id!==id)}
    try{localStorage.setItem(SHORTCUT_KEY,JSON.stringify(next));setLinks(next)}catch{setError('Enregistrement indisponible.')}
  }

  function handleKeys(event){
    if(event.key==='Escape'){event.preventDefault();onClose();return}
    if(event.key!=='Tab')return
    const items=[...event.currentTarget.querySelectorAll('button:not(:disabled),a[href],input,select')].filter(node=>node.offsetParent!==null)
    const first=items[0],last=items.at(-1)
    if(event.shiftKey&&document.activeElement===first){event.preventDefault();last?.focus()}
    else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first?.focus()}
  }

  function tabKey(event,index){
    if(!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return
    event.preventDefault()
    let next=index
    if(event.key==='ArrowRight')next=(index+1)%TABS.length
    if(event.key==='ArrowLeft')next=(index-1+TABS.length)%TABS.length
    if(event.key==='Home')next=0
    if(event.key==='End')next=TABS.length-1
    setTab(TABS[next]);tabRefs.current[next]?.focus()
  }

  return <section ref={dialogRef} className="department-hub" role="dialog" aria-modal="true" aria-labelledby="hub-title" style={{'--hub-color':color}} onKeyDown={handleKeys}>
    <div className="hub-veil" aria-hidden="true"/>
    <header className="hub-header">
      <button className="hub-back" onClick={onClose} aria-label="Retourner au Gate of the Soul"><span aria-hidden="true">←</span> Gate of the Soul</button>
      <p>{system.center} · {system.chakra}</p>
      <button className="hub-memory" onClick={()=>onOpenCenter(system.name)}>Ouvrir dans Mémoire ↗</button>
    </header>

    <nav className="hub-portals" aria-label="Changer de département">
      {systems.map(item=><button key={item.id} aria-label={item.name} className={item.id===system.id?'active':''} aria-current={item.id===system.id?'page':undefined} style={{'--portal-color':`#${item.color.toString(16).padStart(6,'0')}`}} onClick={()=>item.id!==system.id&&onSwitch(item.id)}><i aria-hidden="true"/><span>{item.name}</span></button>)}
    </nav>

    <div className="hub-layout">
      <section className="hub-intro">
        <p className="kicker">{system.center.toUpperCase()} PORTAL</p>
        <h1 id="hub-title">{system.name}</h1>
        <p className="hub-invitation">{system.invitation}</p>
        <div className="hub-statuses">
          <span>{system.status}</span><span>{vault?.noteCount??'—'} notes dans le Vault</span><span>Mode Observer</span>
        </div>
      </section>

      <section className="hub-console" aria-label={`Interface ${system.name}`}>
        <div className="hub-tabs" role="tablist" aria-label="Vues du département">
          {TABS.map((label,index)=><button key={label} ref={node=>{tabRefs.current[index]=node}} id={`tab-${label}`} role="tab" aria-selected={tab===label} aria-controls={`panel-${label}`} tabIndex={tab===label?0:-1} onKeyDown={event=>tabKey(event,index)} onClick={()=>setTab(label)}>{label}</button>)}
        </div>

        {tab==='Portal'&&<div id="panel-Portal" role="tabpanel" aria-labelledby="tab-Portal" className="hub-panel">
          <div className="facet-grid">{system.facets.map((facet,index)=><article key={facet}><small>0{index+1}</small><h2>{facet}</h2><p>{index===0?'Point d’entrée principal du département.':index===1?'Signaux et sources explicitement attribués.':'Une lecture qui respecte les limites d’autorité.'}</p></article>)}</div>
          <div className="hub-note"><span>BOUNDARY</span><p>Cette interface présente les données du Vault. Elle ne lance aucune action et ne modifie aucune vérité institutionnelle.</p></div>
        </div>}

        {tab==='Mémoire'&&<div id="panel-Mémoire" role="tabpanel" aria-labelledby="tab-Mémoire" className="hub-panel memory-panel">
          <div className="panel-heading"><div><small>SOURCES ATTRIBUÉES</small><h2>{nodes.length} document{nodes.length===1?'':'s'}</h2></div><button onClick={()=>onOpenCenter(system.name)}>Toute la mémoire ↗</button></div>
          {nodes.length?<ul>{nodes.slice(0,10).map(node=><li key={node.id||node.path}><button onClick={()=>onOpenNote(node.path,node.title)}><span>{node.title}</span><small>{node.path}</small></button></li>)}</ul>:<div className="empty-memory"><b>Aucune note attribuée directement.</b><p>Les documents non attribués restent disponibles dans la Mémoire commune; ils ne sont pas associés automatiquement à ce département.</p></div>}
        </div>}

        {tab==='Outils'&&<div id="panel-Outils" role="tabpanel" aria-labelledby="tab-Outils" className="hub-panel tools-panel">
          <div className="shortcut-list">{rows.map(row=><article key={row.id}><div><small>{row.kind}</small><a href={row.url} target="_blank" rel="noreferrer">{row.name} ↗</a></div><button onClick={()=>remove(row.id)} aria-label={`Supprimer ${row.name}`}>Supprimer</button></article>)}{!rows.length&&<p>Aucun raccourci local pour ce portail.</p>}</div>
          <form onSubmit={save}>
            <h2>Ajouter un raccourci local</h2>
            <p>Enregistré uniquement dans ce navigateur; ceci ne crée pas une intégration Alpha Proxima.</p>
            <label>Nom<input value={name} onChange={event=>setName(event.target.value)} required maxLength="80"/></label>
            <label>Adresse web<input value={url} onChange={event=>setUrl(event.target.value)} required inputMode="url" placeholder="https://"/></label>
            <label>Type<select value={kind} onChange={event=>setKind(event.target.value)}><option>Outil</option><option>Personne</option><option>Agent</option><option>Dossier</option></select></label>
            <button className="save-shortcut">Enregistrer localement</button>
            <p role="status" className="form-error">{error}</p>
          </form>
        </div>}
      </section>
    </div>
  </section>
}
