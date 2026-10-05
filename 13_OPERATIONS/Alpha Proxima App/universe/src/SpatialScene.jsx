import {useEffect,useRef} from 'react'
import * as THREE from 'three'
import {CAMERA_DISTANCE,IMAGE_SIZE,PORTAL_DURATION_MS,fitArtwork,sampleBody,artworkPoint,smoothstep} from './gate-depth.js'
import {BODY_DEFAULTS,portalLocalPosition,deterministicRandom} from './body-volume.js'
import {createBodyGeometry} from './body-geometry.js'

const placementGLSL = `
  uniform vec2 uImageSize;
  uniform vec2 uImageOffset;
  uniform float uDepth;
  uniform float uTime;
  vec3 placeInField(vec2 point, float relief, float mask) {
    float z = relief * uDepth + mask * sin(uTime * .65) * .012 * uDepth;
    vec2 imagePoint = point * uImageSize + uImageOffset;
    return vec3(imagePoint * (6.0 - z) / 6.0, z);
  }
`

function makeArtwork(texture,uniforms,compact){
  const group=new THREE.Group()
  for(const foreground of [false,true]){
  const geometry=new THREE.PlaneGeometry(1,1,compact?112:184,compact?70:115)
  const uv=geometry.attributes.uv
  const depths=new Float32Array(uv.count),masks=new Float32Array(uv.count)
  for(let i=0;i<uv.count;i++){
    const relief=sampleBody(uv.getX(i),1-uv.getY(i))
    depths[i]=foreground?relief.depth:-.72;masks[i]=foreground?relief.mask:relief.erase
  }
  geometry.setAttribute('aDepth',new THREE.BufferAttribute(depths,1))
  geometry.setAttribute('aMask',new THREE.BufferAttribute(masks,1))
  const material=new THREE.ShaderMaterial({
    uniforms:{...uniforms,uArtwork:{value:texture},uForeground:{value:foreground?1:0}},
    vertexShader:`${placementGLSL}
      attribute float aDepth;
      attribute float aMask;
      varying vec2 vUv;
      varying float vMask;
      uniform float uForeground;
      void main(){
        vUv=uv;vMask=aMask;
        gl_Position=projectionMatrix*modelViewMatrix*vec4(placeInField(position.xy,aDepth,aMask*uForeground),1.0);
      }`,
    fragmentShader:`uniform sampler2D uArtwork;
      uniform float uForeground;uniform float uDepth;uniform float uFlatVisibility;
      varying vec2 vUv;
      varying float vMask;
      void main(){
        if(uForeground>.5&&uFlatVisibility<.01)discard;
        vec4 source=texture2D(uArtwork,vUv);
        if(uForeground>.5){
          if(vMask<.01)discard;
          gl_FragColor=vec4(source.rgb,vMask*uFlatVisibility);
        }else{
          vec4 distantField=texture2D(uArtwork,vec2(.08+(1.0-vUv.x)*.27,vUv.y));
          gl_FragColor=vec4(mix(source.rgb,distantField.rgb,vMask*uDepth),1.0);
        }
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`,
    side:THREE.DoubleSide,transparent:true,depthWrite:false,
  })
  const mesh=new THREE.Mesh(geometry,material)
  mesh.frustumCulled=false
  group.add(mesh)
  }
  return group
}

function makeLivingParticles(texture,uniforms,compact){
  // Sample the artwork's luminous skin; no replacement model or new body asset.
  const canvas=document.createElement('canvas')
  canvas.width=400;canvas.height=250
  const context=canvas.getContext('2d',{willReadFrequently:true})
  if(!context)return null
  context.drawImage(texture.image,0,0,400,250)
  const pixels=context.getImageData(0,0,400,250).data
  const positions=[],colors=[],phases=[],masks=[]
  const color=new THREE.Color()
  const count=compact?1500:4200
  let seed=17041
  const random=()=>{seed=(1664525*seed+1013904223)>>>0;return seed/4294967296}
  for(let attempt=0;attempt<count*24&&phases.length<count;attempt++){
    const u=.37+random()*.48,v=.10+random()*.90,relief=sampleBody(u,v)
    if(relief.mask<.18)continue
    const index=(Math.min(249,Math.floor(v*250))*400+Math.min(399,Math.floor(u*400)))*4
    const luminance=(pixels[index]*.21+pixels[index+1]*.72+pixels[index+2]*.07)/255
    if(random()>luminance*.85+.08)continue
    positions.push(u-.5,.5-v,relief.depth+.02+random()*.40)
    color.setRGB(pixels[index]/255,pixels[index+1]/255,pixels[index+2]/255,THREE.SRGBColorSpace)
    colors.push(color.r,color.g,color.b)
    phases.push(random()*Math.PI*2);masks.push(relief.mask)
  }
  const geometry=new THREE.BufferGeometry()
  geometry.setAttribute('position',new THREE.Float32BufferAttribute(positions,3))
  geometry.setAttribute('color',new THREE.Float32BufferAttribute(colors,3))
  geometry.setAttribute('aPhase',new THREE.Float32BufferAttribute(phases,1))
  geometry.setAttribute('aMask',new THREE.Float32BufferAttribute(masks,1))
  const material=new THREE.ShaderMaterial({
    uniforms:{...uniforms,uPointSize:{value:compact?2.4:3.0}},
    vertexShader:`${placementGLSL}
      attribute float aPhase;
      attribute float aMask;
      attribute vec3 color;
      uniform float uPointSize;
      varying vec3 vColor;
      varying float vAlpha;
      void main(){
        float drift=sin(uTime*.38+aPhase);
        vec3 point=placeInField(position.xy,position.z,aMask);
        point.x+=sin(uTime*.27+aPhase*2.0)*.035*uDepth;
        point.y+=drift*.055*uDepth;
        point.z+=cos(uTime*.38+aPhase)*.09*uDepth;
        vec4 view=modelViewMatrix*vec4(point,1.0);
        gl_Position=projectionMatrix*view;
        gl_PointSize=clamp(uPointSize*5.0/-view.z,1.0,6.0);
        vColor=color;
        vAlpha=uDepth*(.23+.20*sin(aPhase+uTime*.6));
      }`,
    fragmentShader:`uniform float uFlatVisibility;varying vec3 vColor;varying float vAlpha;
      void main(){
        float radius=length(gl_PointCoord-.5)*2.0;
        float glow=pow(max(0.0,1.0-radius),2.0);
        gl_FragColor=vec4(vColor*1.8,glow*vAlpha*uFlatVisibility);
        #include <colorspace_fragment>
      }`,
    transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
  })
  const points=new THREE.Points(geometry,material)
  points.frustumCulled=false
  return points
}

function makeStreams(uniforms,compact){
  const group=new THREE.Group()
  for(let strand=0;strand<5;strand++){
    const vertices=[],phases=[]
    const count=compact?90:150
    for(let i=0;i<count;i++){
      const t=i/(count-1),angle=t*Math.PI*5+strand*Math.PI*.4
      const radius=.027+Math.sin(t*Math.PI)*.084
      const u=.625+Math.sin(angle)*radius,v=.785-t*.69
      vertices.push(u-.5,.5-v,sampleBody(u,v).depth+.11+Math.cos(angle)*.24)
      phases.push(t)
    }
    const geometry=new THREE.BufferGeometry()
    geometry.setAttribute('position',new THREE.Float32BufferAttribute(vertices,3))
    geometry.setAttribute('aProgress',new THREE.Float32BufferAttribute(phases,1))
    const material=new THREE.ShaderMaterial({
      uniforms:{...uniforms,uColor:{value:new THREE.Color(strand%2?0xa679ff:0xffd390)},uOffset:{value:strand*.19}},
      vertexShader:`${placementGLSL}
        attribute float aProgress;varying float vProgress;
        void main(){vProgress=aProgress;vec3 point=placeInField(position.xy,position.z,1.0);gl_Position=projectionMatrix*modelViewMatrix*vec4(point,1.0);}`,
      fragmentShader:`uniform vec3 uColor;uniform float uTime;uniform float uDepth;uniform float uOffset;uniform float uFlatVisibility;varying float vProgress;
        void main(){float pulse=pow(max(0.0,sin(vProgress*20.0-uTime*1.1+uOffset*6.28)),12.0);float fade=sin(vProgress*3.14159);gl_FragColor=vec4(uColor,(.035+pulse*.30)*fade*uDepth*uFlatVisibility);
        #include <colorspace_fragment>
        }`,
      transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    })
    const line=new THREE.Line(geometry,material);line.frustumCulled=false;group.add(line)
  }
  return group
}

function makePortal(system,compact){
  const group=new THREE.Group(),rings=[],arms=[]
  const materialOptions={color:system.color,transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,toneMapped:false}
  for(const [i,radius] of [.084,.137,.195].entries()){
    const ring=new THREE.Mesh(new THREE.TorusGeometry(radius,.0035,5,compact?40:72),new THREE.MeshBasicMaterial({...materialOptions,opacity:.5-i*.08}))
    ring.rotation.set(i*.24,i*.13,0);rings.push(ring);group.add(ring)
  }
  for(let arm=0;arm<3;arm++){
    const points=[]
    for(let i=0;i<100;i++){
      const t=i/99,angle=t*Math.PI*4.8+arm*Math.PI*2/3,radius=.02+t*.205
      points.push(Math.cos(angle)*radius,Math.sin(angle)*radius,-(1-t)*.38)
    }
    const geometry=new THREE.BufferGeometry()
    geometry.setAttribute('position',new THREE.Float32BufferAttribute(points,3))
    const line=new THREE.Line(geometry,new THREE.LineBasicMaterial({...materialOptions,opacity:.45}))
    arms.push(line);group.add(line)
  }
  const core=new THREE.Mesh(new THREE.SphereGeometry(.023,12,8),new THREE.MeshBasicMaterial({...materialOptions,color:0xffffff,opacity:.86}))
  group.add(core)
  const body=sampleBody(...system.anchor)
  group.userData={rings,arms,core,anchor:system.anchor,relief:body.mask>.5?body:{depth:-.72,mask:0}}
  return group
}

function makeStars(compact){
  const positions=[],colors=[]
  let seed=82017
  const random=()=>{seed=(1664525*seed+1013904223)>>>0;return seed/4294967296}
  const gold=new THREE.Color(0xefc185),violet=new THREE.Color(0x9075e8)
  for(let i=0;i<(compact?140:370);i++){
    positions.push((random()-.5)*14,(random()-.5)*10,-.3+random()*3.1)
    const color=random()>.36?gold:violet;colors.push(color.r,color.g,color.b)
  }
  const geometry=new THREE.BufferGeometry()
  geometry.setAttribute('position',new THREE.Float32BufferAttribute(positions,3))
  geometry.setAttribute('color',new THREE.Float32BufferAttribute(colors,3))
  return new THREE.Points(geometry,new THREE.PointsMaterial({size:.016,vertexColors:true,transparent:true,opacity:.30,depthWrite:false,blending:THREE.AdditiveBlending}))
}

function makeVolumetricBeing(texture,uniforms,compact){
  const group=new THREE.Group()
  const bodyGeometry=createBodyGeometry(compact)
  const skin=new THREE.ShaderMaterial({
    uniforms:{...uniforms,uArtwork:{value:texture}},
    vertexShader:`varying vec2 vUv;varying vec3 vNormal;varying vec3 vView;
      void main(){
        vUv=vec2(.5+position.x*992.0/1586.0,.5+position.y);
        vec4 view=modelViewMatrix*vec4(position,1.0);
        vNormal=normalize(normalMatrix*normal);vView=normalize(-view.xyz);
        gl_Position=projectionMatrix*view;
      }`,
    fragmentShader:`uniform sampler2D uArtwork;uniform float uDepth;uniform float uFlatVisibility;
      varying vec2 vUv;varying vec3 vNormal;varying vec3 vView;
      void main(){
        vec3 source=texture2D(uArtwork,vUv).rgb;
        float rim=pow(1.0-abs(dot(normalize(vNormal),normalize(vView))),2.0);
        float light=.22+.45*max(0.0,dot(normalize(vNormal),normalize(vec3(-.6,.8,1.0))));
        float filament=pow(abs(sin(vUv.x*480.0+sin(vUv.y*63.0)*3.0)*cos(vUv.y*510.0+sin(vUv.x*72.0)*4.0)),16.0);
        vec3 energy=mix(vec3(.08,.01,.13),vec3(.55,.25,.05),light+rim*.55);
        gl_FragColor=vec4(source*.02+energy*(.18+rim*1.2)+vec3(1.0,.70,.30)*filament*.8,uDepth*(.04+.82*(1.0-uFlatVisibility)));
        #include <colorspace_fragment>
      }`,
    transparent:true,depthWrite:true,side:THREE.FrontSide,
  })
  const skinMesh=new THREE.Mesh(bodyGeometry,skin);skinMesh.frustumCulled=false;group.add(skinMesh)
  const canvas=document.createElement('canvas');canvas.width=480;canvas.height=300
  const context=canvas.getContext('2d',{willReadFrequently:true})
  if(!context)return group
  context.drawImage(texture.image,0,0,canvas.width,canvas.height)
  const pixels=context.getImageData(0,0,canvas.width,canvas.height).data
  const positions=[],colors=[],phases=[],energy=[]
  const color=new THREE.Color(),random=deterministicRandom(compact?91821:491203)
  const total=compact?3100:7200
  function addPoint(x,y,z,phase,energyValue){
    const u=Math.max(0,Math.min(1,x+.5)),v=Math.max(0,Math.min(1,.5-y))
    const ix=Math.min(canvas.width-1,Math.floor(u*(canvas.width-1))),iy=Math.min(canvas.height-1,Math.floor(v*(canvas.height-1)))
    const index=(iy*canvas.width+ix)*4
    const sourceEnergy=(pixels[index]+pixels[index+1]+pixels[index+2])/765
    color.setRGB(pixels[index]/255,pixels[index+1]/255,pixels[index+2]/255,THREE.SRGBColorSpace)
    if(sourceEnergy<.035){color.set(0x8b63d4)}
    positions.push(x*IMAGE_SIZE.width/IMAGE_SIZE.height,y,z*BODY_DEFAULTS.depthScale);colors.push(color.r,color.g,color.b);phases.push(phase);energy.push(Math.min(1,energyValue+sourceEnergy*.28))
  }
  const surfacePositions=bodyGeometry.attributes.position
  for(let point=0;point<total;point++){
    const index=Math.floor(random()*bodyGeometry.drawRange.count)
    addPoint(surfacePositions.getX(index)*IMAGE_SIZE.height/IMAGE_SIZE.width,surfacePositions.getY(index),surfacePositions.getZ(index)/BODY_DEFAULTS.depthScale,random()*Math.PI*2,.7+random()*.3)
  }
  const geometry=new THREE.BufferGeometry()
  geometry.setAttribute('position',new THREE.Float32BufferAttribute(positions,3))
  geometry.setAttribute('color',new THREE.Float32BufferAttribute(colors,3))
  geometry.setAttribute('aPhase',new THREE.Float32BufferAttribute(phases,1))
  geometry.setAttribute('aEnergy',new THREE.Float32BufferAttribute(energy,1))
  const material=new THREE.ShaderMaterial({
    uniforms:{...uniforms,uPointSize:{value:compact?3.5:4.5}},
    vertexShader:`attribute float aPhase;attribute float aEnergy;attribute vec3 color;uniform float uPointSize;uniform float uDepth;uniform float uTime;varying vec3 vColor;varying float vAlpha;
      void main(){vec3 point=position;float flow=sin(uTime*.42+aPhase)*.012*uDepth;point.x+=flow;point.y+=cos(uTime*.31+aPhase*1.7)*.009*uDepth;point.z+=sin(uTime*.27+aPhase)*.035*uDepth;vec4 view=modelViewMatrix*vec4(point,1.0);gl_Position=projectionMatrix*view;gl_PointSize=clamp(uPointSize*(4.8/-view.z)*(1.0+aEnergy*.45),1.0,7.0);vColor=color;vAlpha=(.19+aEnergy*.34)*uDepth;}`,
    fragmentShader:`varying vec3 vColor;varying float vAlpha;
      void main(){
        float r=length(gl_PointCoord-.5)*2.0;
        float glow=pow(max(0.0,1.0-r),2.4);
        gl_FragColor=vec4(vColor*(1.35+glow*.85),glow*vAlpha);
        #include <colorspace_fragment>
      }`,
    transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
  })
  const particles=new THREE.Points(geometry,material);particles.frustumCulled=false;group.add(particles)

  const threadMaterial=new THREE.LineBasicMaterial({color:0xe8b56b,transparent:true,opacity:.18,depthWrite:false,blending:THREE.AdditiveBlending})
  const spine=[]
  for(let i=0;i<130;i++){const t=i/129;spine.push((.11+Math.sin(t*8)*.018)*IMAGE_SIZE.width/IMAGE_SIZE.height,.30-t*.80,(.12+Math.cos(t*9)*.025)*BODY_DEFAULTS.depthScale)}
  const spineGeometry=new THREE.BufferGeometry();spineGeometry.setAttribute('position',new THREE.Float32BufferAttribute(spine,3));const spineLine=new THREE.Line(spineGeometry,threadMaterial);group.add(spineLine)
  const haloGeometry=new THREE.BufferGeometry(),halo=[]
  for(let ring=0;ring<8;ring++){const y=.22-ring*.09,rx=.06+Math.sin(ring/7*Math.PI)*.09,rz=.18+Math.sin(ring/7*Math.PI)*.28;for(let point=0;point<=56;point++){const angle=point/56*Math.PI*2;halo.push((.11+Math.cos(angle)*rx)*IMAGE_SIZE.width/IMAGE_SIZE.height,y,Math.sin(angle)*rz*BODY_DEFAULTS.depthScale)}}
  haloGeometry.setAttribute('position',new THREE.Float32BufferAttribute(halo,3));const haloLine=new THREE.LineSegments(haloGeometry,new THREE.LineBasicMaterial({color:0x9c7cff,transparent:true,opacity:.10,depthWrite:false,blending:THREE.AdditiveBlending}));group.add(haloLine)
  group.userData={particles,spineLine,haloLine}
  return group
}

export default function SpatialScene({systems,activeId,phase,portalSequence,paused,visible,reducedMotion,forceFallback,onFallback,onProject,onReady,depthEnabled=true,viewResetKey=0}){
  const hostRef=useRef(null),runtimeRef=useRef(null)
  const stateRef=useRef({activeId,phase,paused,visible,reducedMotion,portalSequence,depthEnabled,viewResetKey})
  const callbacksRef=useRef({onFallback,onProject,onReady})
  callbacksRef.current={onFallback,onProject,onReady}

  useEffect(()=>{
    const previous=stateRef.current
    stateRef.current={activeId,phase,paused,visible,reducedMotion,portalSequence,depthEnabled,viewResetKey}
    const runtime=runtimeRef.current
    if(portalSequence!==previous.portalSequence)runtime?.beginPortal()
    if(depthEnabled!==previous.depthEnabled||phase!==previous.phase)runtime?.changeView()
    if(viewResetKey!==previous.viewResetKey)runtime?.recenter()
    runtime?.restart()
  },[activeId,phase,paused,visible,reducedMotion,portalSequence,depthEnabled,viewResetKey])

  useEffect(()=>{
    const host=hostRef.current
    callbacksRef.current.onReady?.(false)
    if(!host||forceFallback){callbacksRef.current.onFallback(true);return}
    let renderer
    try{renderer=new THREE.WebGLRenderer({alpha:true,antialias:window.innerWidth>720,powerPreference:'high-performance'})}
    catch{callbacksRef.current.onFallback(true);return}
    renderer.setClearColor(0x000000,0)
    renderer.outputColorSpace=THREE.SRGBColorSpace
    renderer.domElement.setAttribute('aria-hidden','true')
    host.append(renderer.domElement)
    const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(50,1,.05,40)
    const compact=window.innerWidth<=720
    const uniforms={uDepth:{value:0},uTime:{value:0},uImageSize:{value:new THREE.Vector2()},uImageOffset:{value:new THREE.Vector2()},uFlatVisibility:{value:1},uBodyYaw:{value:0}}
    const stars=makeStars(compact);scene.add(stars)
    const bodyRoot=new THREE.Group(),bodyPivot=new THREE.Group();bodyPivot.rotation.order='YXZ';bodyPivot.position.x=BODY_DEFAULTS.centerX*IMAGE_SIZE.width/IMAGE_SIZE.height;bodyRoot.add(bodyPivot);scene.add(bodyRoot)
    const portals=new Map(systems.map(system=>[system.id,makePortal(system,compact)]))
    portals.forEach(portal=>scene.add(portal))
    const projected={},projectVector=new THREE.Vector3(),baseCamera=new THREE.Vector3(),lookTarget=new THREE.Vector3(),travelTarget=new THREE.Vector3()
    let fit,width=1,height=1,raf=0,last=performance.now(),elapsed=0,portalStarted=0,lastTravel=0
    let manualYaw=0,manualPitch=0,bodyYaw=0,pitch=0,pointerX=0,pointerY=0,drag=null,poseDirty=false,depthRequest=true
    let disposed=false,ready=false,contextLost=false,texture=null,particleField=null,streams=null,reportAt=0,frames=0
    renderer.debug.onShaderError=()=>{
      contextLost=true;ready=false;cancelAnimationFrame(raf)
      renderer.domElement.style.display='none'
      callbacksRef.current.onReady?.(false);callbacksRef.current.onFallback(true)
    }

    function setArtworkFit(){
      fit=fitArtwork(width,height,camera.fov)
      uniforms.uImageSize.value.set(fit.width,fit.height)
      uniforms.uImageOffset.value.set(fit.x,fit.y)
      bodyRoot.position.set(fit.x,fit.y,0)
      bodyRoot.scale.setScalar(fit.height)
    }

    function resize(){
      width=Math.max(1,host.clientWidth);height=Math.max(1,host.clientHeight)
      camera.aspect=width/height;camera.updateProjectionMatrix()
      renderer.setPixelRatio(width<=720?1:Math.min(window.devicePixelRatio||1,1.5))
      renderer.setSize(width,height,false)
      setArtworkFit();restart()
    }

    function renderFrame(now){
      raf=0
      if(disposed||contextLost)return
      const state=stateRef.current
      if(!state.visible){host.dataset.renderState='hidden';return}
      const moving=!state.paused&&!state.reducedMotion&&state.phase!=='hub'
      const dt=Math.min((now-last)/1000,.05);last=now
      if(moving)elapsed+=dt
      const targetDepth=state.phase==='arrival'||!state.depthEnabled?0:1
      const interpolation=moving?1-Math.exp(-dt*2.4):depthRequest?1:0
      uniforms.uDepth.value+=(targetDepth-uniforms.uDepth.value)*interpolation
      depthRequest=false
      if(Math.abs(targetDepth-uniforms.uDepth.value)<.001)uniforms.uDepth.value=targetDepth
      uniforms.uTime.value=elapsed
      const depth=uniforms.uDepth.value
      const travel=state.phase==='portal'?(moving?smoothstep(0,1,(now-portalStarted)/PORTAL_DURATION_MS):lastTravel):state.phase==='hub'?lastTravel:0
      if(state.phase==='portal')lastTravel=travel
      // Passive motion stays gentle. A drag leaves a persistent chosen viewpoint.
      const idleYaw=moving&&state.phase==='gate'?Math.sin(elapsed*.20)*.036:0
      const idlePitch=moving&&state.phase==='gate'?Math.sin(elapsed*.16)*.009:0
      const targetYaw=THREE.MathUtils.clamp(manualYaw+pointerX*.08+idleYaw,-Math.PI,Math.PI)*depth
      const targetPitch=THREE.MathUtils.clamp(manualPitch-pointerY*.020+idlePitch,-BODY_DEFAULTS.pitchLimit,BODY_DEFAULTS.pitchLimit)*depth
      if(moving){bodyYaw+=(targetYaw-bodyYaw)*(1-Math.exp(-dt*5));pitch+=(targetPitch-pitch)*(1-Math.exp(-dt*5))}
      else if(poseDirty){bodyYaw=THREE.MathUtils.clamp(manualYaw,-Math.PI,Math.PI)*depth;pitch=THREE.MathUtils.clamp(manualPitch,-BODY_DEFAULTS.pitchLimit,BODY_DEFAULTS.pitchLimit)*depth}
      poseDirty=false
      bodyPivot.rotation.y=bodyYaw
      bodyPivot.rotation.x=pitch
      bodyRoot.visible=ready&&depth>.005
      uniforms.uBodyYaw.value=bodyYaw
      uniforms.uFlatVisibility.value=1-smoothstep(.22,.78,Math.abs(bodyYaw))

      portals.forEach((portal,id)=>{
        const {anchor,relief,rings,arms,core}=portal.userData
        const point=new THREE.Vector3(...portalLocalPosition(anchor,fit,depth))
        bodyPivot.localToWorld(point)
        portal.position.copy(point)
        const selected=id===state.activeId
        portal.visible=ready&&state.phase!=='arrival'&&state.phase!=='hub'
        const scale=selected?(state.phase==='portal'?1+travel*1.4:1.10):.88
        portal.scale.setScalar(scale)
        portal.rotation.z=elapsed*(selected?.20:.095)
        rings.forEach((ring,i)=>{
          ring.rotation.z=elapsed*(i%2?-.35:.29)*(i+1)
          ring.rotation.x=i*.24+Math.sin(elapsed*.45+i)*.09
          ring.material.opacity=(selected?.65:.30)*(state.phase==='portal'&&!selected?1-travel:1)
        })
        arms.forEach((arm,i)=>{arm.rotation.z=-elapsed*.62+i*.13;arm.material.opacity=(selected?.53:.24)*(state.phase==='portal'&&!selected?1-travel:1)})
        core.visible=state.phase!=='portal'
      })

      // Keep the camera at one stable distance. The body turns inside the
      // frame; a hidden zoom-out on every drag would make the spatial motion
      // feel like a camera transition rather than a free 360° body view.
      const cameraDistance=CAMERA_DISTANCE
      baseCamera.set(0,Math.sin(pitch)*cameraDistance,Math.cos(pitch)*cameraDistance)
      camera.position.copy(baseCamera);lookTarget.set(0,0,0)
      if(travel>0){
        const chosen=portals.get(state.activeId)
        if(chosen){
          travelTarget.copy(chosen.position);travelTarget.z+=.58
          camera.position.lerp(travelTarget,travel*.94)
          lookTarget.copy(chosen.position).multiplyScalar(travel)
        }
      }
      camera.lookAt(lookTarget);camera.updateMatrixWorld()
      stars.material.opacity=(.08+depth*.23)*(1-travel*.55)
      stars.rotation.z=elapsed*.002
      if(particleField)particleField.visible=depth>.005
      if(streams)streams.visible=depth>.005
      renderer.render(scene,camera);frames++

      // DOM controls use the very same transformed coordinates as each portal.
      portals.forEach((portal,id)=>{
        projectVector.copy(portal.position).project(camera)
        projected[id]={left:(projectVector.x+1)*width/2,top:(1-projectVector.y)*height/2}
      })
      if(ready)callbacksRef.current.onProject?.(projected)
      host.dataset.renderState=state.phase==='hub'?'resting':moving?'animated':'paused'
      if(!moving||now-reportAt>500){
        host.dataset.depth=depth.toFixed(3)
        host.dataset.bodyYaw=bodyYaw.toFixed(3)
        host.dataset.renderFrames=String(frames)
        host.dataset.triangles=String(renderer.info.render.triangles)
        reportAt=now
      }
      if(moving&&ready&&!contextLost)raf=requestAnimationFrame(renderFrame)
    }

    function restart(){
      cancelAnimationFrame(raf);last=performance.now()
      if(fit)renderFrame(last)
    }
    function recenter(){manualYaw=0;manualPitch=0;pointerX=0;pointerY=0;poseDirty=true}
    function beginPortal(){portalStarted=performance.now();lastTravel=0;drag=null;host.dataset.dragging='false'}
    function changeView(){depthRequest=true;poseDirty=true}
    runtimeRef.current={restart,recenter,beginPortal,changeView}

    function canExplore(){const s=stateRef.current;return ready&&s.phase==='gate'&&s.depthEnabled&&s.visible}
    function pointerDown(event){
      if(!canExplore()||event.button!==0)return
      drag={id:event.pointerId,x:event.clientX,y:event.clientY,yaw:manualYaw,pitch:manualPitch}
      host.setPointerCapture(event.pointerId);host.dataset.dragging='true'
      host.focus({preventScroll:true})
    }
    function pointerMove(event){
      if(!canExplore())return
      const rect=host.getBoundingClientRect()
      if(drag&&drag.id===event.pointerId){
        manualYaw=THREE.MathUtils.clamp(drag.yaw-(event.clientX-drag.x)/width*Math.PI*2,-Math.PI,Math.PI)
        manualPitch=THREE.MathUtils.clamp(drag.pitch+(event.clientY-drag.y)/height*.24,-BODY_DEFAULTS.pitchLimit,BODY_DEFAULTS.pitchLimit)
        pointerX=0;pointerY=0;poseDirty=true
      }else if(event.pointerType==='mouse'){
        pointerX=(event.clientX-rect.left)/width*2-1;pointerY=(event.clientY-rect.top)/height*2-1
      }
      if(poseDirty&&(stateRef.current.paused||stateRef.current.reducedMotion))restart()
    }
    function pointerUp(event){
      if(drag?.id!==event.pointerId)return
      drag=null;host.dataset.dragging='false'
      if(host.hasPointerCapture(event.pointerId))host.releasePointerCapture(event.pointerId)
    }
    function pointerLeave(){if(!drag){pointerX=0;pointerY=0}}
    function keyDown(event){
      if(!canExplore()||!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Home'].includes(event.key))return
      event.preventDefault()
      if(event.key==='Home')recenter()
      else if(event.key==='ArrowLeft')manualYaw=Math.max(-Math.PI,manualYaw-.16)
      else if(event.key==='ArrowRight')manualYaw=Math.min(Math.PI,manualYaw+.16)
      else if(event.key==='ArrowUp')manualPitch=Math.min(BODY_DEFAULTS.pitchLimit,manualPitch+.015)
      else if(event.key==='ArrowDown')manualPitch=Math.max(-BODY_DEFAULTS.pitchLimit,manualPitch-.015)
      poseDirty=true
      restart()
    }
    function lostContext(event){
      event.preventDefault();contextLost=true;ready=false;cancelAnimationFrame(raf)
      renderer.domElement.style.display='none'
      callbacksRef.current.onReady?.(false);callbacksRef.current.onFallback(true)
    }
    host.addEventListener('pointerdown',pointerDown)
    host.addEventListener('pointermove',pointerMove)
    host.addEventListener('pointerup',pointerUp)
    host.addEventListener('pointercancel',pointerUp)
    host.addEventListener('pointerleave',pointerLeave)
    host.addEventListener('keydown',keyDown)
    renderer.domElement.addEventListener('webglcontextlost',lostContext)
    const observer=new ResizeObserver(resize);observer.observe(host);resize()

    new THREE.TextureLoader().load(`${import.meta.env.BASE_URL}assets/alpha-hero-gold-v2.jpg`,loaded=>{
      if(disposed||contextLost){loaded.dispose();return}
      texture=loaded;texture.colorSpace=THREE.SRGBColorSpace
      texture.anisotropy=Math.min(4,renderer.capabilities.getMaxAnisotropy())
      scene.add(makeArtwork(texture,uniforms,compact))
      const volume=makeVolumetricBeing(texture,uniforms,compact)
      volume.position.x=-BODY_DEFAULTS.centerX*IMAGE_SIZE.width/IMAGE_SIZE.height
      bodyPivot.add(volume)
      try{particleField=makeLivingParticles(texture,uniforms,compact);if(particleField)scene.add(particleField)}catch{/* Artwork and portals remain usable if pixel sampling is unavailable. */}
      streams=makeStreams(uniforms,compact);scene.add(streams)
      ready=true;restart()
      if(!contextLost){callbacksRef.current.onFallback(false);callbacksRef.current.onReady?.(true)}
    },undefined,()=>{
      if(disposed)return
      callbacksRef.current.onReady?.(false);callbacksRef.current.onFallback(true)
    })

    return()=>{
      disposed=true;runtimeRef.current=null;cancelAnimationFrame(raf);observer.disconnect()
      host.removeEventListener('pointerdown',pointerDown);host.removeEventListener('pointermove',pointerMove)
      host.removeEventListener('pointerup',pointerUp);host.removeEventListener('pointercancel',pointerUp)
      host.removeEventListener('pointerleave',pointerLeave);host.removeEventListener('keydown',keyDown)
      renderer.domElement.removeEventListener('webglcontextlost',lostContext)
      scene.traverse(object=>{object.geometry?.dispose();if(Array.isArray(object.material))object.material.forEach(material=>material.dispose());else object.material?.dispose()})
      texture?.dispose();renderer.dispose();renderer.domElement.remove()
    }
  },[forceFallback])

  return <div ref={hostRef} className="gate-scene" role="region" aria-label="Vue spatiale du Gate of the Soul" aria-description="Glisse pour explorer. Au clavier : flèches pour déplacer le regard, touche Origine pour recentrer." tabIndex={phase==='gate'&&depthEnabled&&!forceFallback?0:-1}/>
}
