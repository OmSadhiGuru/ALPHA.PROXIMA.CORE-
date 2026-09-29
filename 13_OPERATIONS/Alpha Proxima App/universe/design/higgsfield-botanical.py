"""Alpha Proxima: portable botanical interior, authored for Higgsfield Blender.

Run in Blender 5.2 with bpy available. This file creates ONLY a decorative
overlay; the existing humanoid and chakra centers remain in the web renderer.
Blender (x, depth, height) exports to glTF (x, height, -depth), unscaled.
No external assets, texture files, add-ons, or network requests are required.
The service can export the scene as GLB after execution. Preview is rendered
to /tmp/alpha-proxima-botanical-preview.png; publish that path through the
service's artifact API. Cameras and lights are outside Botanical_Overlay.
"""

import bpy
import math
import random
from mathutils import Vector


SEED = 92826
RNG = random.Random(SEED)
PREVIEW = artifacts.file(name='alpha-proxima-botanical-preview.png', media_type='image/png')
PREVIEW_PATH = str(PREVIEW.path)

# A fresh private Higgsfield scene: prevent a default cube from entering export.
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
collection = bpy.data.collections.new('Botanical_Overlay')
bpy.context.scene.collection.children.link(collection)


def material(name, color, roughness=.52, metallic=.08, emission=0):
    mat = bpy.data.materials.new('Botanical_' + name)
    mat.use_nodes = True
    mat.diffuse_color = (*color, 1)
    mat.use_backface_culling = False
    shader = mat.node_tree.nodes.get('Principled BSDF')
    shader.inputs['Base Color'].default_value = (*color, 1)
    shader.inputs['Roughness'].default_value = roughness
    shader.inputs['Metallic'].default_value = metallic
    shader.inputs['Alpha'].default_value = 1
    shader.inputs['Emission Color'].default_value = (*color, 1)
    shader.inputs['Emission Strength'].default_value = emission
    return mat


materials = {
    'PetalRose': material('PetalRose', (.50, .115, .275), .43),
    'PetalLilac': material('PetalLilac', (.30, .205, .52), .46),
    'PetalPearl': material('PetalPearl', (.54, .38, .57), .5),
    'LeafTeal': material('LeafTeal', (.055, .235, .21), .61),
    'Stem': material('Stem', (.075, .17, .155), .56),
    'Pollen': material('Pollen', (.44, .28, .19), .39, .22),
    'Filament': material('Filament', (.045, .34, .49), .34, .08, 1.1),
}
geometry = {name: {'vertices': [], 'faces': []} for name in materials}


def add_geometry(name, vertices, faces):
    bucket = geometry[name]
    offset = len(bucket['vertices'])
    bucket['vertices'].extend(tuple(v) for v in vertices)
    bucket['faces'].extend(tuple(offset + i for i in f) for f in faces)


def frame(direction):
    tangent = Vector(direction).normalized()
    helper = Vector((0, 0, 1)) if abs(tangent.z) < .88 else Vector((1, 0, 0))
    side = tangent.cross(helper).normalized()
    up = side.cross(tangent).normalized()
    return tangent, side, up


def tube(points, radius, name='Stem', sides=6, taper=.35):
    """Closed mesh tube: thin physical stems, never camera-facing lines."""
    points = [Vector(p) for p in points]
    vertices, faces = [], []
    for i, point in enumerate(points):
        direction = points[min(i + 1, len(points) - 1)] - points[max(i - 1, 0)]
        _, side, up = frame(direction)
        r = radius * (1 - taper * i / (len(points) - 1))
        for j in range(sides):
            a = 2 * math.pi * j / sides
            vertices.append(point + r * (side * math.cos(a) + up * math.sin(a)))
        if i:
            for j in range(sides):
                a = (i - 1) * sides + j
                b = (i - 1) * sides + (j + 1) % sides
                faces.append((a, b, i * sides + (j + 1) % sides, i * sides + j))
    faces.append(tuple(reversed(range(sides))))
    faces.append(tuple((len(points) - 1) * sides + j for j in range(sides)))
    add_geometry(name, vertices, faces)


def bezier(a, b, c, d, count=18):
    a, b, c, d = map(Vector, (a, b, c, d))
    return [(1-t)**3*a + 3*(1-t)**2*t*b + 3*(1-t)*t*t*c + t**3*d
            for t in (i / (count - 1) for i in range(count))]


def blade(origin, direction, normal, length, width, name, curl=.28, twist=.1):
    """Curved pointed petal/leaf mesh with a lifted midrib and tapered tip."""
    origin, axis = Vector(origin), Vector(direction).normalized()
    normal = Vector(normal)
    normal = (normal - axis * normal.dot(axis)).normalized()
    side = axis.cross(normal).normalized()
    vertices, faces = [], []
    rows, columns = 8, 5
    for i in range(rows):
        u = i / (rows - 1)
        # The first/last row retains a tiny width to avoid degenerate normals.
        spread = width * (.012 + math.sin(math.pi * u) ** .83)
        for j in range(columns):
            v = 2 * j / (columns - 1) - 1
            lift = length * (curl*u*u + .105*(1-v*v)*math.sin(math.pi*u))
            drift = length * twist * math.sin(math.pi*u) * u
            vertices.append(origin + axis*(length*u) + side*(v*spread + drift)
                            + normal*(lift + length*.065*v*v*math.sin(math.pi*u)))
    for i in range(rows - 1):
        for j in range(columns - 1):
            a = i*columns + j
            faces.append((a, a+1, a+columns+1, a+columns))
    add_geometry(name, vertices, faces)
    return origin + axis*length + normal*(length*curl)


def seed_head(center, radius, normal, name='Pollen'):
    """Small lentil-shaped flower disk; petals carry the flower silhouette."""
    center, normal = Vector(center), Vector(normal).normalized()
    _, side, up = frame(normal)
    vertices = [center + normal*radius*.32, center - normal*radius*.2]
    count = 10
    for i in range(count):
        angle = 2*math.pi*i/count
        vertices.append(center + radius*(math.cos(angle)*side + math.sin(angle)*up))
    faces = []
    for i in range(count):
        a, b = 2+i, 2+(i+1) % count
        faces.extend(((0, a, b), (1, b, a)))
    add_geometry(name, vertices, faces)


# Side vines stay outside |x| < .18. Depth undulation gives a changing
# silhouette in front/profile/back views, while the central chakra line stays open.
vines = []
for sign in (-1, 1):
    main = bezier((sign*.27, .07, .26), (sign*.50, -.14, .79),
                  (sign*.22, .08, 1.60), (sign*.69, -.075, 2.22), 34)
    tube(main, .010, sides=7, taper=.57)
    vines.append(main)
    shoulder = bezier((sign*.39, -.015, 1.80), (sign*.57, -.075, 2.08),
                      (sign*.74, .06, 2.22), (sign*.89, .025, 2.10), 20)
    tube(shoulder, .0068, sides=6, taper=.7)
    vines.append(shoulder)
    # Fine neck/head side branch; never runs over brow or crown centers.
    head = bezier((sign*.34, .05, 2.18), (sign*.26, .10, 2.58),
                  (sign*.245, -.025, 3.02), (sign*.25, -.045, 3.47), 28)
    tube(head, .0048, sides=5, taper=.72)
    vines.append(head)

# Sparse leaves alternate along physical stems. Their pointed curved surfaces
# replace billboard foliage; repeated material buckets keep draw calls low.
for vine_index, vine in enumerate(vines):
    sign = -1 if vine_index < 3 else 1
    indices = (5, 12, 19, 26) if len(vine) > 30 else (5, 12, 18)
    for leaf_index, idx in enumerate(indices):
        if idx >= len(vine)-1:
            continue
        origin = vine[idx]
        length = RNG.uniform(.085, .16) if vine_index % 3 != 2 else RNG.uniform(.055, .085)
        outward = sign * (1 if leaf_index % 2 == 0 else .18)
        direction = Vector((outward, RNG.uniform(-.8, .75), RNG.uniform(.35, .8)))
        normal = Vector((sign*.13, -1, .18)).normalized()
        blade(origin, direction, normal, length, length*.28, 'LeafTeal', .20,
              RNG.uniform(-.15, .15))
        vein_end = origin + direction.normalized()*length*.86 + normal*length*.12
        tube([origin, origin.lerp(vein_end, .55)+normal*.008, vein_end],
             .0015, 'Filament', 4, .75)


# (x, depth, height, petal length, palette). 14 asymmetric blossoms, with
# smaller head/neck blooms and room for the user's seven center spheres.
flowers = [
    (-.34, -.13, .40, .080, 'PetalRose'),
    ( .36,  .075, .56, .084, 'PetalLilac'),
    (-.37, -.18, .88, .108, 'PetalLilac'),
    ( .39, -.13, 1.12, .112, 'PetalRose'),
    (-.36,  .10, 1.34, .094, 'PetalPearl'),
    ( .40,  .10, 1.54, .090, 'PetalLilac'),
    (-.48, -.12, 1.76, .120, 'PetalRose'),
    ( .53, -.11, 1.95, .111, 'PetalPearl'),
    (-.70, -.09, 2.15, .126, 'PetalLilac'),
    ( .78,  .025, 2.14, .104, 'PetalRose'),
    (-.31,  .035, 2.46, .058, 'PetalPearl'),
    ( .25, -.095, 3.02, .058, 'PetalLilac'),
    (-.26, -.07, 3.28, .068, 'PetalRose'),
    ( .265, .025, 3.43, .064, 'PetalPearl'),
]

for index, (x, depth, z, size, palette) in enumerate(flowers):
    center = Vector((x, depth, z))
    side_sign = -1 if x < 0 else 1
    # Face some flowers front, some sideways, some toward the back of the shell.
    depth_facing = .78 if index in (1, 4, 5, 9, 13) else -1
    normal = Vector((side_sign*RNG.uniform(.1, .62), depth_facing,
                     RNG.uniform(.12, .65))).normalized()
    _, u_axis, v_axis = frame(normal)
    phase = RNG.uniform(0, math.pi)
    petal_count = 6 + index % 3
    for ring, fraction, count in ((0, 1, petal_count), (1, .57, 5)):
        for i in range(count):
            angle = phase + 2*math.pi*i/count + ring*.4
            direction = u_axis*math.cos(angle) + v_axis*math.sin(angle)
            origin = center + normal*(ring*.014) + direction*(size*.04)
            blade(origin, direction, normal, size*fraction*RNG.uniform(.86, 1.1),
                  size*fraction*RNG.uniform(.31, .42),
                  palette if ring == 0 else 'PetalPearl',
                  .24 + ring*.19, RNG.uniform(-.11, .11))
    seed_head(center+normal*.018, size*.19, normal)
    for i in range(5):
        angle = phase + i*math.tau/5
        offset = (u_axis*math.cos(angle) + v_axis*math.sin(angle))*size*.095
        end = center + offset + normal*(size*.35)
        tube([center+offset, center+offset+normal*size*.2, end],
             .0018, 'Pollen', 4, .3)
        seed_head(end, .0045, normal, 'Filament' if i == 0 else 'Pollen')
    # A real branch links every blossom to a neighboring vine.
    candidates = [p for vine in vines for p in vine if p.x*x > 0]
    source = min(candidates, key=lambda p: (p-center).length_squared)
    branch = bezier(source, source+Vector((side_sign*.018, .025, .025)),
                    center-normal*.035, center, 9)
    tube(branch, .0036, sides=5, taper=.6)

# Seven slender cyan threads meander with the vines, below emissive bloom
# saturation. They have real depth and do not cross the body center line.
for index, vine in enumerate(vines):
    thread = [p + Vector((math.sin(i*.41)*.013, .026+math.cos(i*.37)*.016, .006))
              for i, p in enumerate(vine)]
    tube(thread, .0019 if index % 3 != 2 else .0013, 'Filament', 4, .45)

mesh_objects = []
for name, bucket in geometry.items():
    mesh = bpy.data.meshes.new('Botanical_' + name + '_Geometry')
    mesh.from_pydata(bucket['vertices'], [], bucket['faces'])
    mesh.update()
    obj = bpy.data.objects.new('Botanical_' + name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(materials[name])
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    mesh_objects.append(obj)


def aim(obj, point):
    obj.rotation_euler = (Vector(point) - obj.location).to_track_quat('-Z', 'Y').to_euler()


def point_light(name, location, energy, color, size):
    light = bpy.data.lights.new(name, 'POINT')
    light.energy, light.color, light.shadow_soft_size = energy, color, size*.25
    obj = bpy.data.objects.new(name, light)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    aim(obj, (0, 0, 1.7))
    return obj


scene = bpy.context.scene
world = bpy.data.worlds.new('Botanical_NavyWorld')
world.use_nodes = True
world.node_tree.nodes['Background'].inputs['Color'].default_value = (.002, .004, .012, 1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value = .3
scene.world = world
point_light('Delivery_Key', (3, -5, 6), 650, (.72, .84, 1), 4)
point_light('Delivery_Fill', (-4, -2, 3), 330, (.7, .53, .85), 3)
point_light('Delivery_Rim', (1, 3, 4), 600, (.29, .64, .9), 3)
camera_data = bpy.data.cameras.new('Delivery_Camera')
camera = bpy.data.objects.new('Delivery_Camera', camera_data)
scene.collection.objects.link(camera)
camera.location = (9, -18, 6)
aim(camera, (0, 0, 1.85))
camera_data.type = 'ORTHO'
camera_data.ortho_scale = 4.2
scene.camera = camera
scene.render.engine = 'BLENDER_EEVEE'
scene.render.resolution_x = 512
scene.render.resolution_y = 768
scene.render.resolution_percentage = 100
scene.render.image_settings.media_type = 'IMAGE'
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False
scene.render.filepath = PREVIEW_PATH
scene.view_settings.view_transform = 'AgX'

all_vertices = [v.co for obj in mesh_objects for v in obj.data.vertices]
minimum = [min(v[i] for v in all_vertices) for i in range(3)]
maximum = [max(v[i] for v in all_vertices) for i in range(3)]
vertex_count = sum(len(obj.data.vertices) for obj in mesh_objects)
triangle_count = sum(sum(len(face.vertices)-2 for face in obj.data.polygons) for obj in mesh_objects)
assert vertex_count < 30000, 'Overlay vertex budget exceeded'
assert len(mesh_objects) < 20, 'Overlay draw-call budget exceeded'
result = {
    'name': 'Alpha Proxima botanical interior',
    'seed': SEED,
    'flowers': len(flowers),
    'mesh_count': len(mesh_objects),
    'vertex_count': vertex_count,
    'triangle_count': triangle_count,
    'blender_bounds_min': minimum,
    'blender_bounds_max': maximum,
    'gltf_bounds_min': [minimum[0], minimum[2], -maximum[1]],
    'gltf_bounds_max': [maximum[0], maximum[2], -minimum[1]],
    'gltf_scale': 1,
    'mesh_prefix': 'Botanical_',
    'overlay_collection': 'Botanical_Overlay',
    'preview_path': PREVIEW_PATH,
    'note': 'Overlay only: no humanoid, chakra spheres, floor, images, or textures.',
}
bpy.ops.render.render(write_still=True)
PREVIEW.publish()
print(result)
