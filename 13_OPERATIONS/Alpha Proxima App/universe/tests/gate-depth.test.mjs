import test from 'node:test'
import assert from 'node:assert/strict'
import {Euler,PerspectiveCamera,Vector3} from 'three'
import {artworkPoint,CAMERA_DISTANCE,fitArtwork,sampleBody,silhouetteDistance} from '../src/gate-depth.js'
import {BODY_DEFAULTS,portalLocalPosition} from '../src/body-volume.js'
import {baseSystems} from '../src/systems.js'

const viewports=[
  [1280,800],[1440,900],[1920,1080],
  [390,844],[320,568],[430,932],[768,1024],
]

function cameraFor(width,height,yaw=0,pitch=0){
  const camera=new PerspectiveCamera(50,width/height,.1,30)
  const distance=CAMERA_DISTANCE
  camera.position.set(0,Math.sin(pitch)*distance,Math.cos(pitch)*distance)
  camera.lookAt(0,0,0)
  camera.updateMatrixWorld()
  return camera
}

function screenPoint(point,camera,width,height){
  const projected=new Vector3(point.x,point.y,point.z).project(camera)
  return {x:(projected.x+1)*width/2,y:(1-projected.y)*height/2,z:projected.z}
}

function expectedCover(u,v,width,height){
  // The browser's object-fit:cover, with the approved portrait object-position.
  const scale=Math.max(width/1586,height/992)
  return {
    x:(width-1586*scale)*(width<=720?.61:.5)+u*1586*scale,
    y:(height-992*scale)/2+v*992*scale,
  }
}

function close(actual,expected,message){
  assert.ok(Math.abs(actual-expected)<1e-7,`${message}: ${actual} != ${expected}`)
}

function portalPoint(system,amount,fit,time=0){
  const body=sampleBody(...system.anchor)
  const surface=body.mask>.5?body:{depth:-.72,mask:0}
  const point=artworkPoint(...system.anchor,surface.depth,amount,fit,time,surface.mask)
  // The actual scene keeps portal cores just in front of their chosen layer.
  return {...point,z:point.z+.025}
}

function rotatedPortalPoint(system,amount,fit,yaw=0,pitch=0){
  const local=new Vector3(...portalLocalPosition(system.anchor,fit,amount))
  local.applyEuler(new Euler(pitch,yaw,0,'YXZ'))
  local.x+=BODY_DEFAULTS.centerX*1586/992
  local.multiplyScalar(fit.height)
  const center=new Vector3(fit.x,fit.y,0)
  return local.add(center)
}

test('both artwork layers preserve frontal source coordinates at every depth and viewport',()=>{
  const samples=[[0,0],[1,0],[0,1],[1,1],[.5,.5],...baseSystems.map(system=>system.anchor)]
  for(const [width,height] of [...viewports,[844,390]]){
    const camera=cameraFor(width,height)
    const fit=fitArtwork(width,height)
    for(const [u,v] of samples){
      const body=sampleBody(u,v)
      const expected=expectedCover(u,v,width,height)
      for(const layer of [body,{depth:-.72,mask:0}]){
        for(const amount of [0,.35,1]){
          for(const time of [0,3.2]){
            const point=artworkPoint(u,v,layer.depth,amount,fit,time,layer.mask)
            const screen=screenPoint(point,camera,width,height)
            close(screen.x,expected.x,`horizontal source registration at ${width}x${height}`)
            close(screen.y,expected.y,`vertical source registration at ${width}x${height}`)
            assert.ok(screen.z>-1&&screen.z<1,'each artwork layer remains inside camera clipping planes')
          }
        }
      }
    }
  }
})

test('the separate body sculpture has finite masks and shallow bounded depth',()=>{
  let minimum=Infinity,maximum=-Infinity
  for(let row=0;row<=100;row++){
    for(let column=0;column<=100;column++){
      const u=column/100,v=row/100
      const {mask,depth,erase}=sampleBody(u,v)
      assert.ok([mask,depth,erase,silhouetteDistance(u,v)].every(Number.isFinite))
      assert.ok(mask>=0&&mask<=1,'the silhouette mask must be a valid blend weight')
      assert.ok(erase>=0&&erase<=1,'background replacement must be a valid blend weight')
      assert.ok(depth>=.42&&depth<=1.2,'the foreground must stay in its shallow positive-depth band')
      minimum=Math.min(minimum,depth)
      maximum=Math.max(maximum,depth)
    }
  }
  assert.ok(maximum-minimum>.6,'the body itself retains a sculpted surface')
  assert.ok(maximum-minimum<.8,'foreground vertices never descend into the background plane')
  assert.ok(maximum-(-.72)>1.8,'the separate field has perceptible separation behind the body')
})

test('the head, torso and pelvis belong to the foreground while distant sky does not',()=>{
  for(const [u,v] of [[.607,.214],[.596,.481],[.603,.718]]){
    const body=sampleBody(u,v)
    assert.ok(silhouetteDistance(u,v)>0,'body interiors have a positive signed distance')
    assert.equal(body.mask,1,'the head, torso and pelvis are fully opaque foreground')
    assert.ok(body.depth>.8,'the body is in front of the neutral image plane')
    assert.equal(body.erase,1,'the distant plane replaces the hidden copy of the body')
  }
  for(const [u,v] of [[.1,.1],[.1,.5],[.9,.1],[.95,.9]]){
    const body=sampleBody(u,v)
    assert.ok(silhouetteDistance(u,v)<0,'sky has a negative signed distance')
    assert.equal(body.mask,0,'distant sky is discarded from the foreground sculpture')
    assert.equal(body.erase,0,'visible distant sky retains the original source pixels')
  }
})

test('the crown glow remains original source artwork outside the body sculpture',()=>{
  const crown=baseSystems.find(system=>system.id==='LUMIAION')
  const [u,v]=crown.anchor
  for(const [dx,dy] of [[0,0],[-.012,0],[.012,0],[0,-.01],[0,.01]]){
    const body=sampleBody(u+dx,v+dy)
    assert.equal(body.mask,0,'the floating crown glow is part of the distant image layer')
    assert.equal(body.erase,0,'the crown glow must never be replaced by borrowed cosmos')
  }
})

test('all seven chakra anchors remain visible and registered in desktop and portrait views',()=>{
  assert.equal(baseSystems.length,7)
  for(const [width,height] of viewports){
    const fit=fitArtwork(width,height)
    const camera=cameraFor(width,height)
    for(const system of baseSystems){
      const [u,v]=system.anchor
      for(const amount of [0,1]){
        const screen=screenPoint(rotatedPortalPoint(system,amount,fit),camera,width,height)
        assert.ok(screen.x>=26&&screen.x<=width-26,`${system.id} retains a horizontal touch margin at ${width}x${height}`)
        assert.ok(screen.y>=26&&screen.y<=height-26,`${system.id} retains a vertical touch margin at ${width}x${height}`)
        const expected=expectedCover(u,v,width,height)
        assert.ok(Math.abs(screen.x-expected.x)<2.5,`${system.id} remains visually registered horizontally despite its tiny front offset`)
        assert.ok(Math.abs(screen.y-expected.y)<2.5,`${system.id} remains visually registered vertically despite its tiny front offset`)
      }
    }
  }
})

test('all seven controls retain touch margins throughout the bounded exploration range',()=>{
  for(const [width,height] of viewports){
    const fit=fitArtwork(width,height)
    // A complete body turn keeps the centers on the volumetric being.
    for(const yaw of [-Math.PI,-Math.PI/2,0,Math.PI/2,Math.PI]){
      for(const pitch of [-BODY_DEFAULTS.pitchLimit,BODY_DEFAULTS.pitchLimit]){
        const camera=cameraFor(width,height,yaw,pitch)
        for(const system of baseSystems){
          const screen=screenPoint(rotatedPortalPoint(system,1,fit,yaw,pitch),camera,width,height)
          assert.ok(screen.x>=26&&screen.x<=width-26,`${system.id} retains horizontal touch margin while exploring ${width}x${height}`)
          assert.ok(screen.y>=26&&screen.y<=height-26,`${system.id} retains vertical touch margin while exploring ${width}x${height}`)
        }
      }
    }
  }
})

test('camera movement reveals real depth while the flat state stays registered',()=>{
  const width=1280,height=800,fit=fitArtwork(width,height)
  const body=sampleBody(.63,.4)
  const near=rotatedPortalPoint({anchor:[.85,.4]},1,fit,.18,0)
  const far=rotatedPortalPoint({anchor:[.85,.4]},1,fit,-.18,0)
  const front=cameraFor(width,height)
  const initialNear=screenPoint(near,front,width,height)
  const initialFar=screenPoint(far,front,width,height)
  assert.ok(Math.abs(initialNear.x-initialFar.x)>1,'a modest full-body turn produces perceptible lateral movement')
  close(near.y,far.y,'a horizontal turn preserves world-space height; perspective changes screen-space height')
  assert.ok(BODY_DEFAULTS.yawLimit>=Math.PI,'the interaction supports a complete turn')
  const flatNear=artworkPoint(.63,.4,body.depth,0,fit)
  const flatFar=artworkPoint(.63,.4,-.72,0,fit)
  close(screenPoint(flatNear,front,width,height).x,screenPoint(flatFar,front,width,height).x,'2D mode removes depth parallax horizontally')
  close(screenPoint(flatNear,front,width,height).y,screenPoint(flatFar,front,width,height).y,'2D mode removes depth parallax vertically')
})
