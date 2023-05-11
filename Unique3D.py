
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
c=0
opt_texture = [
    'arrow_down',
    'arrow_right',
    'brick',
    'circle',
    'circle_outlined',
    'cobblestone',
    'cursor',
    'file_icon',
    'folder',
    'grass',
    'heightmap_1',
    'horizontal_gradient',
    'noise',
    'radial_gradient',
    'reflection_map_3',
    'shore',
    'sky_default',
    'sky_sunset',
    'ursina_logo',
    'ursina_wink_0000',
    'ursina_wink_0001',
    'vertical_gradient',
    # 'white_cube',
]

class Voxel(Button):
    def __init__(self, position=(0,0,0), 
                 texture='white_cube',
                 default_color=color.white,
                 ):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            highlight_color=color.red,
            color=default_color,
        )

# for y in range(10,101,50):
#     for z in range(12):
#         for x in range(12):
#             voxel = Voxel(position=(x,y,z))

with open('input/UNIQUE.txt') as f:
    plain = f.read()

for i, z in enumerate(plain.split('\n')):
    for j, x in enumerate(list(z)):
        if int(x):
            Voxel(position=(i,0,j))
        else:
            Voxel(
            position=(i,0,j),
            default_color=color.black,
            )

def input(key):
    hit_info = raycast(camera.world_position, camera.forward, distance=100)
    global c
    c+=1

    if key == 'left mouse down':
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal, 
                #   texture='brick',
                #   default_color=color.orange,
                  texture=opt_texture[c%len(opt_texture)],
                  default_color=color.random_color(),
                  )
            
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

    try:
        if key == 'e': # teleporting at center of screen
            player.x = hit_info.entity.position.x
            player.y = hit_info.entity.position.y
            player.z = hit_info.entity.position.z
    except:
        pass

    if key == 'f': # press f for anti-gravity
        player.gravity *= -1

window.fullscreen = 1
player = FirstPersonController(gravity=.1)

def update():
    # pass
    if player.y < -10 or player.y > 250:
        player.y = 150

Sky()
app.run()
