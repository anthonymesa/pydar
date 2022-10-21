from re import M
from pyray import *

init_window(1500, 500, "Hello")

camera = Camera3D((50,0,0), (0,0,0), (0,1,0), 90, CAMERA_PERSPECTIVE)

castle_model = load_model("../res/models/castle/castle.obj")
castle_texture = load_texture("../res/models/castle/castle_diffuse.png")

set_material_texture(castle_model.materials[0], MATERIAL_MAP_DIFFUSE, castle_texture)

set_camera_mode(camera, CAMERA_FREE)
set_target_fps(60)

while not window_should_close():

    update_camera(camera)

    begin_drawing()

    clear_background(WHITE)

    begin_mode_3d(camera)

    draw_model(castle_model, (0,-15,0), 1, WHITE)

    end_mode_3d()

    end_drawing()

unload_texture(castle_texture)
unload_model(castle_model)
close_window()