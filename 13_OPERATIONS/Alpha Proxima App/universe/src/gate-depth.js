// A front-view sculpture of the approved artwork. The shape describes visual
// depth only; the original pixels remain the material across the entire field.
export const IMAGE_SIZE = {width:1586,height:992}
export const CAMERA_DISTANCE = 6
export const PORTAL_DURATION_MS = 1250

const volumes = [
  [.607,.214,.052,.093,.94], [.638,.215,.029,.068,1],
  [.608,.303,.034,.065,.78], [.596,.481,.089,.177,1.06],
  [.515,.388,.047,.077,.86], [.668,.405,.043,.074,.89],
  [.480,.490,.033,.103,.76], [.446,.615,.031,.091,.66],
  [.416,.748,.027,.069,.58], [.700,.518,.027,.094,.74],
  [.741,.676,.036,.096,.64], [.795,.800,.041,.063,.56],
  [.603,.718,.087,.106,.88], [.550,.886,.049,.172,.84],
  [.649,.900,.052,.183,.81],
]

// The silhouette keeps foreground skin and its glow separate from the distant
// field, so oblique views expose space instead of stretching background pixels.
const silhouette=[
  [.610,.138],[.635,.151],[.650,.184],[.650,.203],[.644,.214],
  [.654,.228],[.645,.250],[.635,.265],[.632,.292],[.638,.316],
  [.668,.337],[.695,.370],[.712,.414],[.714,.461],[.722,.510],
  [.721,.570],[.743,.633],[.760,.693],[.779,.741],[.807,.755],
  [.835,.786],[.825,.805],[.831,.820],[.818,.841],[.802,.862],
  [.783,.856],[.771,.835],[.763,.786],[.746,.770],[.728,.734],
  [.708,.699],[.681,.661],[.670,.620],[.664,.560],[.661,.560],
  [.668,.640],[.675,.709],[.687,.772],[.701,.841],[.707,.925],
  [.703,1.03],[.636,1.03],[.625,.930],[.609,.818],[.594,.887],
  [.575,.946],[.563,1.03],[.500,1.03],[.509,.950],[.505,.909],
  [.509,.842],[.518,.780],[.532,.713],[.539,.654],[.542,.615],
  [.536,.575],[.516,.542],[.501,.530],[.489,.578],[.476,.625],
  [.460,.665],[.443,.699],[.435,.733],[.437,.773],[.441,.799],
  [.432,.819],[.417,.810],[.405,.790],[.397,.763],[.392,.725],
  [.399,.705],[.417,.685],[.429,.640],[.438,.592],[.451,.551],
  [.462,.495],[.471,.449],[.474,.398],[.487,.354],[.512,.326],
  [.541,.315],[.568,.309],[.580,.292],[.574,.270],[.560,.236],
  [.555,.202],[.563,.167],[.583,.145],
]

export function silhouetteDistance(u,v){
  let inside=false,distance=Infinity
  for(let i=0,j=silhouette.length-1;i<silhouette.length;j=i++){
    const [ax,ay]=silhouette[j],[bx,by]=silhouette[i]
    if((ay>v)!==(by>v)&&u<(bx-ax)*(v-ay)/(by-ay)+ax)inside=!inside
    const dx=bx-ax,dy=by-ay
    const t=Math.max(0,Math.min(1,((u-ax)*dx+(v-ay)*dy)/(dx*dx+dy*dy)))
    distance=Math.min(distance,Math.hypot(u-ax-t*dx,v-ay-t*dy))
  }
  return inside?distance:-distance
}

export function smoothstep(low,high,value){
  const t=Math.min(1,Math.max(0,(value-low)/(high-low)))
  return t*t*(3-2*t)
}

export function sampleRelief(u,v){
  let mask=0,volume=0
  for(const [x,y,rx,ry,height] of volumes){
    const radius=Math.hypot((u-x)/rx,(v-y)/ry)
    const edge=1-smoothstep(.82,1.22,radius)
    mask=Math.max(mask,edge)
    volume=Math.max(volume,edge*(.34+height*Math.sqrt(Math.max(0,1-radius*radius))))
  }
  const background=-.72+.09*Math.sin(u*13+v*9)*Math.sin(v*17)
  return {mask,depth:background*(1-mask)+volume}
}

export function sampleBody(u,v){
  const distance=silhouetteDistance(u,v)
  const {depth}=sampleRelief(u,v)
  return {
    mask:smoothstep(-.015,.006,distance),
    // The body itself remains a connected shallow sculpture. The surrounding
    // background is an independent plane, not a steep skirt of image triangles.
    depth:.42+smoothstep(-.012,.065,distance)*.48+Math.max(0,depth)*.18,
    erase:smoothstep(-.022,-.007,distance)*(smoothstep(.7,1.2,Math.hypot((u-.617)/.033,(v-.109)/.027))),
  }
}

export function fitArtwork(width,height,fov=50){
  const viewHeight=2*Math.tan(fov*Math.PI/360)*CAMERA_DISTANCE
  const worldPerPixel=viewHeight/height
  const scale=Math.max(width/IMAGE_SIZE.width,height/IMAGE_SIZE.height)
  const pixelWidth=IMAGE_SIZE.width*scale,pixelHeight=IMAGE_SIZE.height*scale
  const left=(width-pixelWidth)*(width<=720?.61:.5)
  const top=(height-pixelHeight)*.5
  return {
    width:pixelWidth*worldPerPixel,height:pixelHeight*worldPerPixel,
    x:(left+pixelWidth/2-width/2)*worldPerPixel,
    y:-(top+pixelHeight/2-height/2)*worldPerPixel,
    pixelWidth,pixelHeight,left,top,
  }
}

// Pinhole compensation keeps the reference identical from the front even as
// its surface acquires depth. Surface, filaments and hit targets share this map.
export function artworkPoint(u,v,depth,amount,fit,time=0,mask=0){
  const z=depth*amount+mask*Math.sin(time*.65)*.012*amount
  const perspective=(CAMERA_DISTANCE-z)/CAMERA_DISTANCE
  return {
    x:((u-.5)*fit.width+fit.x)*perspective,
    y:((.5-v)*fit.height+fit.y)*perspective,
    z,
  }
}
