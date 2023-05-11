
from ursina import *
app = Ursina()

video = 'video/smileGIFintoBinaryencodedQRcodeYOUTUBEasINFINITEFILESTORAGEimvickykumar999.mp4'
video_player = Entity(model='quad', parent=camera.ui, texture=video)
video_sound = loader.loadSfx(video)

video_player.texture.synchronizeTo(video_sound)
video_sound.play()
app.run()
