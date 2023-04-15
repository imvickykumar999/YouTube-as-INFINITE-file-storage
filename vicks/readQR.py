
# pip install pyzbar
from moviepy.editor import VideoFileClip
from pyzbar.pyzbar import decode
import numpy as np, os, shutil
import split_file as yt
from PIL import Image

SAVING_FRAMES_PER_SECOND = 1

def QRjson(file = "input/1.jpg"):
    out = decode(Image.open(file))
    print(out)

    if len(out):
        out = out[0].data.decode('utf-8')
        return out
    else:
        return '\n'

# QRjson()

def main(video_file, mode):
    video_clip = VideoFileClip(video_file)
    filename = "input"

    try:
        os.mkdir(filename)
    except:
        pass

    try:
        os.mkdir('files')
    except:
        pass

    saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second

    for current_duration in np.arange(0, video_clip.duration, step):
        frame_filename = os.path.join(filename, f"{int(current_duration)+1}.jpg")

        video_clip.save_frame(frame_filename, current_duration)
        line = QRjson(frame_filename)

        fileout, ext = os.path.splitext(video_file)
        with open(f"files/{fileout.split('/')[1] +ext}.txt", mode) as myfile:
            myfile.write(line)
        mode = "a"


if __name__=='__main__':
    # video_file = 'video/InternshipDetails.mp4'
    video_file = input('Enter file name from `video` folder or YouTube or Instagram Reel `link` : ')
    
    try:
        video_file = yt.ytvideo(video_file)
    except:
        pass

    try:
        video_file = yt.instavideo(video_file)
    except:
        pass

    main('video/' + video_file, "w")

input('\n\tPress any key to delete input folder')
shutil.rmtree('input')
