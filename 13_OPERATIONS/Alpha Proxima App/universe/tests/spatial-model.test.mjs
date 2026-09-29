import test from 'node:test'
import assert from 'node:assert/strict'
import fs from 'node:fs'
import * as THREE from 'three'
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js'
import {baseSystems} from '../src/systems.js'
const bytes=fs.readFileSync(new URL('../public/assets/auric-human.glb',import.meta.url))
const gltf=await new GLTFLoader().parseAsync(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),'')
const mixer=new THREE.AnimationMixer(gltf.scene);mixer.clipAction(gltf.animations.find(a=>a.name==='idle')).play();mixer.update(.1);gltf.scene.updateMatrixWorld(true)
const box=new THREE.Box3().setFromObject(gltf.scene),scale=7.6/box.getSize(new THREE.Vector3()).y,center=box.getCenter(new THREE.Vector3())
const bone=name=>gltf.scene.getObjectByName(name).getWorldPosition(new THREE.Vector3()).sub(center).multiplyScalar(scale)
test('human mesh has genuine front-to-back depth and posed limbs',()=>{assert(box.getSize(new THREE.Vector3()).z*scale>1);assert(bone('mixamorigHead').y>bone('mixamorigHips').y);let skinned=0;gltf.scene.traverse(o=>{if(o.isSkinnedMesh)skinned++});assert(skinned>=1)})
test('centers follow the requested anatomical order against the model',()=>{const [crown,eye,throat,heart,solar,sacral,root]=baseSystems.map(s=>s.position[1]);assert(crown>3.8);assert(eye>bone('mixamorigHead').y&&eye<bone('mixamorigHeadTop_End').y);assert(Math.abs(throat-bone('mixamorigNeck').y)<.15);assert(Math.abs(heart-bone('mixamorigSpine2').y)<.2);assert(heart>solar&&solar>sacral&&sacral>root);assert(sacral>bone('mixamorigHips').y);assert(root<bone('mixamorigHips').y&&root>bone('mixamorigHips').y-.5)})
test('chakra colors remain purple indigo blue green yellow orange red',()=>{assert.deepEqual(baseSystems.map(s=>s.color),[0xb85cff,0x5145cd,0x279eff,0x36da78,0xffdd28,0xff8a22,0xf02d45])})
