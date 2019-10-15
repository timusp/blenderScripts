import bpy

for scene in bpy.data.scenes:
    for object in scene.objects:
        for modifier in object.modifiers:
            if modifier.type == 'FLUID_SIMULATION':
                if modifier.settings.type == 'DOMAIN':
                    bpy.ops.fluid.bake({'scene': scene, 'active_object': object})
                    break
