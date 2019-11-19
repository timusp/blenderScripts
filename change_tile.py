import bpy

for scene in bpy.data.scenes:
    scene.render.tile_x = 32
    scene.render.tile_y = 32
    scene.cycles.tile_order = 'RIGHT_TO_LEFT'
