
import zipfile
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.all as vfx


input = 'static/Bed Bugs.mp3'
output = 'static/output.zip'

def compress_zip(input):
    print('Zipping...')
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as f:
        f.write(input)
    print('Zipped.')

# compress_zip(input)


def decompress_unzip():
    print('Unzipping...')
    with zipfile.ZipFile(output, 'r') as f:
        f.extractall('.')
    print('Unzipped.')

# decompress_unzip()


in_loc = 'static/_config.yml.avi'
out_loc = 'static/compressed.mp4'

def framerate(in_loc, out_loc):
    videoclip = VideoFileClip(in_loc)
    videoclip = videoclip.set_fps(videoclip.fps * 2)
    videoclip = videoclip.fx(vfx.speedx, 10)

    videoclip = videoclip.without_audio()
    # audioclip = AudioFileClip("static/Bed Bugs.mp3")
    # videoclip = videoclip.set_audio(audioclip)
    videoclip.write_videofile(out_loc)

# framerate(in_loc, out_loc)
