
# pip install pyzbar
from moviepy.editor import VideoFileClip
from pyzbar.pyzbar import decode
import numpy as np, os, shutil
from PIL import Image

SAVING_FRAMES_PER_SECOND = 1

def QRjson(file):
    out = decode(Image.open(file))
    out = out[0].data.decode('utf-8')
    return out

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
        print(line)

        fileout, ext = os.path.splitext(video_file)
        with open(f"files/{fileout.split('/')[1] +ext}.txt", mode) as myfile:
            myfile.write(line)
        mode = "a"
        


# video_file = 'video/InternshipDetails.mp4'
video_file = 'video/' + input('Enter file name from video folder : ')
main(video_file, "w")

input('Press any key to delete input folder')
shutil.rmtree('input')
