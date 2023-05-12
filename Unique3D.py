
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
t = time.time()
c=0

opt_texture = [
    'arrow_down',
    'arrow_right',
    'brick',
    'circle',
    'circle_outlined',
    # 'cobblestone',
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

mario  = Audio('static/super-mario-bros.mp3',  loop = True,  autoplay = True)
fall   = Audio('static/Super Mario Death.mp3', loop = False, autoplay = False)
winner = Audio('static/Super Mario Won.mp3',   loop = True,  autoplay = False)
cont = True

class Voxel(Button):
    def __init__(self, position=(0,0,0), 
                 texture='static/wall.png',
                 default_color=color.white,
                 ):
        super().__init__(
            parent=scene,
            position=position,
            collider='box',
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
            
        # else:
        #     Voxel(
        #     position=(i,-1,j),
        #     default_color=color.random_color(), 
        #     texture='white_cube',          
        #     # default_color=color.white,
        #     )

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
player = FirstPersonController(collider='box', 
                               model='sphere', 
                               color=color.yellow,
                               texture='heightmap_1')

player.gravity = 10e-2
player.x = 1
player.y = 2
player.z = 1

def update():
    global deatils, player, won, cont
    tc = time.time()
    
    if player.y < -10 or player.y > 100: # respawn
        player.y = 100

    if (player.y < -5) or (tc - t > 100):
        won.text = 'You Lost'
        won.color = color.red

        mario.pause()
        if cont:
            cont = False
            fall.play()
        
    if player.z > 158 and player.y > -1:
        won.text = 'You Won'

        mario.pause()
        if cont:
            cont = False
            winner.play()
        
    deatils.text = f'''
    Score = {int(player.z)}
    Time left = {int(100 - (tc - t))} sec.
    '''

deatils = Text(
    origin=(.1, -4),
	font='VeraMono.ttf', 
	color=color.white,
	) 

won = Text(
    origin=(0,-4),
	color=color.green,
	) 

skybox_image = load_texture("static/space.png")
sky = Sky(texture=skybox_image)

# Sky()
app.run()
