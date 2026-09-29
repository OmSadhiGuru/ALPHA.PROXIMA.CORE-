import { useEffect, useRef, useState } from 'react'
import * as THREE from 'three'
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import { MeshSurfaceSampler } from 'three/addons/math/MeshSurfaceSampler.js'
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js'
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js'
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js'
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js'

export default function SpatialScene({ mode, embodiment, selected, viewRequest, onSelect, onOpenNote, systems, nodes }) {
  const mount = useRef(null)
  const state = useRef({})
  const [status,setStatus] = useState('Chargement du corps en volume…')
  const [botanicalError,setBotanicalError] = useState(false)
  state.current = {mode,embodiment,selected,viewRequest,onSelect,onOpenNote,systems,nodes}
  useEffect(() => {
    const host=mount.current, scene=new THREE.Scene()
    scene.background=new THREE.Color('#02040a')
    const camera=new THREE.PerspectiveCamera(42,1,.015,160)
    const renderer=new THREE.WebGLRenderer({antialias:true})
    renderer.setPixelRatio(Math.min(devicePixelRatio,1.75))
    renderer.outputColorSpace=THREE.SRGBColorSpace
    renderer.toneMapping=THREE.ACESFilmicToneMapping
    renderer.toneMappingExposure=1.05
    host.appendChild(renderer.domElement)
    const composer=new EffectComposer(renderer)
    composer.addPass(new RenderPass(scene,camera))
    const bloom=new UnrealBloomPass(new THREE.Vector2(1,1),.42,.35,.7)
    composer.addPass(bloom);composer.addPass(new OutputPass())
    const controls=new OrbitControls(camera,renderer.domElement)
    controls.enableDamping=true;controls.dampingFactor=.075;controls.enablePan=true
    controls.minDistance=.035;controls.maxDistance=35;controls.zoomSpeed=.7
    const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches
    const body=new THREE.Group(), interior=new THREE.Group(), knowledge=new THREE.Group(), botanical=new THREE.Group()
    scene.add(body,interior,knowledge,botanical)
    const botanicalMaterials=new Set()
    scene.add(new THREE.HemisphereLight(0x8fcfff,0x100620,2.4))
    const light=new THREE.DirectionalLight(0x8ddbff,3.3);light.position.set(3,4,6);scene.add(light)
    const rim=new THREE.DirectionalLight(0xbe62ea,3);rim.position.set(-3,1,-4);scene.add(rim)
    const shellMaterial=new THREE.MeshPhysicalMaterial({color:0x426b8c,metalness:.2,roughness:.24,transparent:true,opacity:.23,depthWrite:false,side:THREE.DoubleSide,clearcoat:1})
    const softenPoints=material=>{
      material.onBeforeCompile=shader=>{
        shader.vertexShader=shader.vertexShader.replace('#include <logdepthbuf_vertex>','gl_PointSize = min(gl_PointSize, 9.0);\n#include <logdepthbuf_vertex>')
        shader.fragmentShader=shader.fragmentShader.replace('#include <color_fragment>','#include <color_fragment>\nfloat radius = length(gl_PointCoord - vec2(0.5)); if(radius > 0.5) discard; diffuseColor.a *= pow(1.0 - radius * 2.0, 1.6);')
      };return material
    }
    const pointMaterial=softenPoints(new THREE.PointsMaterial({size:.018,vertexColors:true,transparent:true,opacity:.65,depthWrite:false,blending:THREE.AdditiveBlending}))
    const skinMeshes=[],beacons=[],hitTargets=[]
    let disposed=false,frame,lastMode='',lastSelected='',lastView=-1,previousNodes=null,transition=null
    const clock=new THREE.Clock()
    const front=new THREE.Vector3(0,0,1)
    const fitDistance=()=>{
      const h=host.clientHeight,w=host.clientWidth
      const usefulH=w<900?Math.max(190,h-290):Math.max(260,h-340)
      return Math.max(11.8,4.3/Math.tan(THREE.MathUtils.degToRad(21))*h/usefulH,3.1/(w/h)/Math.tan(THREE.MathUtils.degToRad(21)))
    }
    camera.position.set(0,.15,fitDistance());controls.target.set(0,.15,0)
    const makeCurve=(points,color,opacity=.35)=>{
      const curve=new THREE.CatmullRomCurve3(points)
      const line=new THREE.Line(new THREE.BufferGeometry().setFromPoints(curve.getPoints(28)),new THREE.LineBasicMaterial({color,transparent:true,opacity,depthWrite:false,blending:THREE.AdditiveBlending}))
      interior.add(line);return line
    }
    systems.forEach(system=>{
      const anchor=new THREE.Group();anchor.position.fromArray(system.position)
      const core=new THREE.Mesh(new THREE.SphereGeometry(.085,24,16),new THREE.MeshBasicMaterial({color:system.color,toneMapped:false}))
      const halo=new THREE.Mesh(new THREE.SphereGeometry(.12,24,16),new THREE.MeshBasicMaterial({color:system.color,transparent:true,opacity:.12,depthWrite:false,side:THREE.DoubleSide}))
      const hit=new THREE.Mesh(new THREE.SphereGeometry(.23,12,8),new THREE.MeshBasicMaterial({visible:false}))
      hit.userData.systemId=system.id;anchor.add(core,halo,hit);interior.add(anchor)
      beacons.push({anchor,core,halo,system});hitTargets.push(hit)
    })
    // One spatial network, shared across all viewpoints. No screen-facing body image.
    makeCurve(systems.map(s=>new THREE.Vector3(...s.position)),0xa088e8,.24)
    new GLTFLoader().load(import.meta.env.BASE_URL+'assets/auric-human.glb',gltf=>{
      if(disposed)return
      const source=gltf.scene,mixer=new THREE.AnimationMixer(source)
      const idle=gltf.animations.find(c=>c.name==='idle')
      if(idle){mixer.clipAction(idle).play();mixer.update(.1)}
      source.updateMatrixWorld(true)
      const box=new THREE.Box3().setFromObject(source),center=box.getCenter(new THREE.Vector3()),scale=7.6/box.getSize(new THREE.Vector3()).y
      const normalize=v=>v.sub(center).multiplyScalar(scale)
      const segments=[]
      source.traverse(object=>{
        if(object.isBone&&object.parent?.isBone){
          const a=normalize(object.parent.getWorldPosition(new THREE.Vector3())),b=normalize(object.getWorldPosition(new THREE.Vector3()))
          if(a.distanceTo(b)>.09)segments.push([a,b])
        }
      })
      source.traverse(object=>{
        if(!object.isMesh)return
        const old=object.geometry,positions=new Float32Array(old.attributes.position.count*3),v=new THREE.Vector3()
        for(let i=0;i<old.attributes.position.count;i++){
          object.getVertexPosition(i,v);v.applyMatrix4(object.matrixWorld);normalize(v);v.toArray(positions,i*3)
        }
        const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.BufferAttribute(positions,3))
        if(old.index)geometry.setIndex(old.index.clone());geometry.computeVertexNormals()
        const mesh=new THREE.Mesh(geometry,shellMaterial);body.add(mesh);skinMeshes.push(mesh)
        const sampler=new MeshSurfaceSampler(mesh).build(),count=object.geometry.attributes.position.count>5000?5500:1600
        const particles=new Float32Array(count*3),colors=new Float32Array(count*3),c=new THREE.Color()
        for(let i=0;i<count;i++){
          sampler.sample(v);v.toArray(particles,i*3)
          c.setHSL(.52+.22*(.5+.5*Math.sin(v.y*1.8+v.x*3)),.55,.46+Math.random()*.22);c.toArray(colors,i*3)
        }
        const dots=new THREE.BufferGeometry();dots.setAttribute('position',new THREE.BufferAttribute(particles,3));dots.setAttribute('color',new THREE.BufferAttribute(colors,3));body.add(new THREE.Points(dots,pointMaterial))
        // Volume samples lie between the posed skeleton and real skin; entering the
        // body reveals these same lights rather than switching to another scene.
        const volumePositions=new Float32Array(2800*3),volumeColors=new Float32Array(2800*3)
        for(let i=0;i<2800;i++){
          sampler.sample(v);let closest=new THREE.Vector3(),distance=Infinity
          for(const [a,b] of segments){const q=new THREE.Line3(a,b).closestPointToPoint(v,true,new THREE.Vector3());const d=q.distanceToSquared(v);if(d<distance){distance=d;closest.copy(q)}}
          closest.lerp(v,.25+Math.random()*.65);closest.toArray(volumePositions,i*3)
          c.setHSL(.55+Math.random()*.28,.7,.52);c.toArray(volumeColors,i*3)
        }
        const volumeGeometry=new THREE.BufferGeometry();volumeGeometry.setAttribute('position',new THREE.BufferAttribute(volumePositions,3));volumeGeometry.setAttribute('color',new THREE.BufferAttribute(volumeColors,3))
        interior.add(new THREE.Points(volumeGeometry,softenPoints(new THREE.PointsMaterial({size:.012,vertexColors:true,transparent:true,opacity:.7,depthWrite:false,blending:THREE.AdditiveBlending}))))
        // Branch toward real sampled skin positions through the nearest bone segment.
        for(let i=0;i<180;i++){
          sampler.sample(v);const end=v.clone().multiplyScalar(.96)
          let nearest=new THREE.Vector3(),distance=Infinity
          for(const [a,b] of segments){const point=new THREE.Line3(a,b).closestPointToPoint(end,true,new THREE.Vector3());const d=point.distanceToSquared(end);if(d<distance){distance=d;nearest.copy(point)}}
          if(!segments.length)nearest.set(0,end.y,0)
          const midpoint=nearest.clone().lerp(end,.55);midpoint.z+=.07*Math.sin(i)
          const color=end.y>2.6?0x8067ff:end.y>1.65?0x36d6b0:end.y>1.15?0xf2d750:end.y>.5?0xf99845:0xe96baf
          makeCurve([nearest,midpoint,end],color,.19)
        }
      })
      for(const [a,b] of segments){const mid=a.clone().lerp(b,.5);mid.z+=.06;makeCurve([a,mid,b],0x71baf4,.32)}
      // Release imported resources after baking the posed geometry.
      source.traverse(o=>{if(o.isMesh){o.geometry.dispose();(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>m.dispose())}})
      mixer.stopAllAction();mixer.uncacheRoot(source)
      setStatus('')
    },undefined,()=>{if(!disposed)setStatus('Le modèle 3D ne peut pas être chargé. Recharge la page.')})
    // Higgsfield's exported mesh shares this field's coordinates in every view.
    // Lighting and camera remain owned by the app; the asset contributes geometry.
    new GLTFLoader().load(import.meta.env.BASE_URL+'assets/higgsfield-botanical.glb',gltf=>{
      if(disposed){gltf.scene.traverse(o=>{o.geometry?.dispose();if(o.material)(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>m.dispose())});return}
      const extras=[]
      gltf.scene.traverse(o=>{
        if(o.isLight||o.isCamera)extras.push(o)
        if(o.isMesh)(Array.isArray(o.material)?o.material:[o.material]).forEach(material=>{
          material.transparent=true;material.depthWrite=false;material.side=THREE.DoubleSide
          botanicalMaterials.add(material)
        })
      })
      extras.forEach(o=>o.removeFromParent());botanical.add(gltf.scene);setBotanicalError(false)
    },undefined,()=>{if(!disposed)setBotanicalError(true)})
    const starPos=new Float32Array(2200*3)
    for(let i=0;i<starPos.length;i+=3){const v=new THREE.Vector3().randomDirection().multiplyScalar(25+Math.random()*65);v.toArray(starPos,i)}
    const starGeo=new THREE.BufferGeometry();starGeo.setAttribute('position',new THREE.BufferAttribute(starPos,3))
    scene.add(new THREE.Points(starGeo,new THREE.PointsMaterial({color:0x90b7d8,size:.035,transparent:true,opacity:.55})))
    const freeResources=group=>{group.traverse(o=>{o.geometry?.dispose();if(o.material)(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>m.dispose())});group.clear()}
    const updateKnowledge=()=>{
      freeResources(knowledge)
      state.current.nodes.slice(0,100).forEach((node,i)=>{
        const owner=systems.find(s=>s.id===node.department)
        if(!owner)return // Unassigned notes stay in Memory, not a guessed department.
        const angle=i*2.39996,r=.3+(i%4)*.095
        const position=new THREE.Vector3(...owner.position).add(new THREE.Vector3(Math.cos(angle)*r,Math.sin(angle)*r*.55,Math.sin(angle*1.7)*r))
        const point=new THREE.Mesh(new THREE.SphereGeometry(.033,10,8),new THREE.MeshBasicMaterial({color:owner.color}));point.position.copy(position);point.userData.note=node;knowledge.add(point)
      })
    }
    // Keep input live: starting a drag or zoom interrupts the camera journey.
    const moveTo=(position,target)=>{transition={from:camera.position.clone(),to:position,fromTarget:controls.target.clone(),target,started:performance.now()}}
    const navigate=()=>{
      const s=state.current,center=systems.find(c=>c.id===s.selected)||systems[0],anchor=new THREE.Vector3(...center.position)
      let direction=camera.position.clone().sub(controls.target).normalize();if(direction.lengthSq()<.5)direction.copy(front)
      const explicit=s.viewRequest?.sequence!==lastView
      if(explicit){lastView=s.viewRequest?.sequence;const view=s.viewRequest?.view;if(view==='front')direction.set(0,0,1);if(view==='side')direction.set(1,0,.04);if(view==='back')direction.set(0,0,-1)}
      if(s.mode==='orbit')moveTo(new THREE.Vector3(0,.15,0).addScaledVector(direction,fitDistance()),new THREE.Vector3(0,.15,0))
      else if(s.mode==='surface')moveTo(anchor.clone().addScaledVector(direction,host.clientWidth<900?4.5:3.2),anchor)
      else {
        // Enter just behind the chosen center and look outward through that same tissue.
        const insideAnchor=anchor.clone();if(center.id==='LUMIAION')insideAnchor.y=3.42
        const eye=insideAnchor.clone().add(new THREE.Vector3(0,0,-.16))
        moveTo(eye,insideAnchor.clone().add(new THREE.Vector3(0,-.7,.05)))
      }
    }
    const pointer=new THREE.Vector2(),ray=new THREE.Raycaster();let down=null
    const pointerDown=e=>{down={x:e.clientX,y:e.clientY}}
    const pointerUp=e=>{
      if(!down||Math.hypot(e.clientX-down.x,e.clientY-down.y)>7)return
      const rect=renderer.domElement.getBoundingClientRect();pointer.set((e.clientX-rect.left)/rect.width*2-1,-(e.clientY-rect.top)/rect.height*2+1);ray.setFromCamera(pointer,camera)
      const hit=ray.intersectObjects([...hitTargets,...knowledge.children])[0]
      if(hit?.object.userData.systemId)state.current.onSelect(hit.object.userData.systemId)
      else if(hit?.object.userData.note?.path){const n=hit.object.userData.note;state.current.onOpenNote(n.path,n.title)}
    }
    const cancelTransition=()=>{transition=null;controls.enabled=true}
    controls.addEventListener('start',cancelTransition)
    renderer.domElement.addEventListener('pointerdown',pointerDown);renderer.domElement.addEventListener('pointerup',pointerUp)
    const resize=()=>{if(state.current.mode==='orbit'){const direction=camera.position.clone().sub(controls.target).normalize();camera.position.copy(controls.target).addScaledVector(direction,fitDistance());transition=null;controls.enabled=true}renderer.setSize(host.clientWidth,host.clientHeight);composer.setSize(host.clientWidth,host.clientHeight);camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix()}
    const observer=new ResizeObserver(resize);observer.observe(host);resize()
    const animate=()=>{
      if(disposed)return
      const t=clock.getElapsedTime(),s=state.current
      if(s.mode!==lastMode||s.selected!==lastSelected||s.viewRequest?.sequence!==lastView){lastMode=s.mode;lastSelected=s.selected;navigate()}
      if(s.nodes!==previousNodes){previousNodes=s.nodes;updateKnowledge()}
      if(transition){const p=reduced?1:Math.min(1,(performance.now()-transition.started)/1250),ease=p*p*(3-2*p);camera.position.lerpVectors(transition.from,transition.to,ease);controls.target.lerpVectors(transition.fromTarget,transition.target,ease);if(p===1){transition=null;controls.enabled=true}}
      shellMaterial.opacity=s.embodiment==='neural'?.045:s.mode==='inward'?.22:.23
      pointMaterial.opacity=s.embodiment==='neural'?.15:s.mode==='inward'?.65:.62
      botanical.visible=s.embodiment==='organic'
      for(const material of botanicalMaterials)material.opacity=s.mode==='inward'?.34:.82
      for(const {core,halo,system} of beacons){const inside=s.mode==='inward'&&s.selected===system.id;core.visible=!inside;halo.visible=!inside;const pulse=reduced?1:1+Math.sin(t*1.6)*.065;core.scale.setScalar(s.mode==='inward'?.35:1);halo.scale.setScalar(pulse*(s.mode==='inward'?.35:1))}
      camera.fov=THREE.MathUtils.lerp(camera.fov,s.mode==='inward'?72:42,.09);camera.updateProjectionMatrix()
      controls.update();composer.render();frame=requestAnimationFrame(animate)
    };animate()
    return()=>{disposed=true;cancelAnimationFrame(frame);observer.disconnect();controls.dispose();renderer.domElement.removeEventListener('pointerdown',pointerDown);renderer.domElement.removeEventListener('pointerup',pointerUp);freeResources(scene);composer.dispose();renderer.dispose();renderer.domElement.remove()}
  },[])
  return <><div className="space" ref={mount} aria-label="Corps humain volumétrique, rotation libre et exploration intérieure" />{status&&<div className="model-status" role="status">{status}</div>}{botanicalError&&<small className="botanical-status" role="status">Couche végétale indisponible · le corps reste accessible</small>}</>
}
