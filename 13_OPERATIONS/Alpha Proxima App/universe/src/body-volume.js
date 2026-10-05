import {IMAGE_SIZE,artworkPoint,sampleBody} from './gate-depth.js'

export const BODY_DEFAULTS={centerX:.11,yawLimit:Math.PI,pitchLimit:.04,depthScale:.38}

export function deterministicRandom(seed=1){
  let state=seed>>>0
  return ()=>{state=(1664525*state+1013904223)>>>0;return state/4294967296}
}

// One coordinate map drives both the rendered portal and its accessible
// button. Compensate perspective before rotation to preserve the source art.
export function portalLocalPosition(anchor,fit,amount=1){
  const surface=sampleBody(...anchor)
  const z=surface.mask>.5?Math.min(.09,surface.depth*.08)*amount:0
  const frontal=artworkPoint(...anchor,z*fit.height,1,fit)
  return [
    (frontal.x-fit.x)/fit.height-BODY_DEFAULTS.centerX*IMAGE_SIZE.width/IMAGE_SIZE.height,
    (frontal.y-fit.y)/fit.height,z,
  ]
}
