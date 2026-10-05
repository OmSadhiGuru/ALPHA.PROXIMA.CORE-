import {MeshBasicMaterial} from 'three'
import {MarchingCubes} from 'three/addons/objects/MarchingCubes.js'
import {IMAGE_SIZE,silhouetteDistance} from './gate-depth.js'

// Reconstruct a closed energy surface from the approved silhouette. The
// unseen profile is an interpretation; the reference contains only one view.
export function createBodyGeometry(compact=false){
  const resolution=compact?42:60
  const temporaryMaterial=new MeshBasicMaterial()
  const surface=new MarchingCubes(resolution,temporaryMaterial,false,false,40000)
  surface.isolation=0
  for(let z=0;z<resolution;z++){
    for(let y=0;y<resolution;y++){
      for(let x=0;x<resolution;x++){
        const px=.18+(x/resolution*2-1)*.43
        const py=-.08+(y/resolution*2-1)*.55
        const pz=(z/resolution*2-1)*.24
        const distance=silhouetteDistance(.5+px*IMAGE_SIZE.height/IMAGE_SIZE.width,.5-py)*IMAGE_SIZE.width/IMAGE_SIZE.height
        surface.setCell(x,y,z,Math.min(distance-pz*pz/.08,.095-Math.abs(pz)))
      }
    }
  }
  surface.update()
  const geometry=surface.geometry.clone()
  const position=geometry.attributes.position
  for(let i=0;i<position.count;i++)position.setXYZ(i,.18+position.getX(i)*.43,-.08+position.getY(i)*.55,position.getZ(i)*.24)
  geometry.computeVertexNormals()
  geometry.computeBoundingSphere()
  surface.geometry.dispose();temporaryMaterial.dispose()
  return geometry
}
