import test from 'node:test'
import assert from 'node:assert/strict'
import {Vector3,Raycaster,Mesh,MeshBasicMaterial,DoubleSide} from 'three'
import {createBodyGeometry} from '../src/body-geometry.js'

for(const compact of [false,true]){
  test(`the ${compact?'mobile':'desktop'} body has raycastable front, side and back surfaces`,()=>{
    const geometry=createBodyGeometry(compact)
    const material=new MeshBasicMaterial({side:DoubleSide})
    const mesh=new Mesh(geometry,material)
    mesh.updateMatrixWorld(true)
    for(const [origin,direction] of [
      [[.18,.03,2],[0,0,-1]],[[.18,.03,-2],[0,0,1]],
      [[2,.03,0],[-1,0,0]],[[-2,.03,0],[1,0,0]],
    ]){
      const hits=new Raycaster(new Vector3(...origin),new Vector3(...direction)).intersectObject(mesh)
      assert.ok(hits.length>=2,'a ray enters and exits the volume')
    }
    assert.ok(geometry.drawRange.count/3<40000,'geometry fits its fixed triangle budget')
    const positions=geometry.attributes.position
    for(let i=0;i<geometry.drawRange.count;i++)assert.ok([positions.getX(i),positions.getY(i),positions.getZ(i)].every(Number.isFinite))
    geometry.dispose();material.dispose()
  })
}
