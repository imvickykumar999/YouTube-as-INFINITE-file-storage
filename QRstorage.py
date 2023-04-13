
from moviepy.editor import VideoFileClip, AudioFileClip
from vicks import split_file as sf
import moviepy.video.fx.all as vfx
import qrcode, os, cv2
from PIL import Image

img = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=5,
)

Image.MAX_IMAGE_PIXELS = 933120000
inp_file = 'input/really_big_file.txt'
sf.split(inp_file)

dirFiles = os.listdir('vicks/output')
dirFiles.sort(key=lambda f: int(f.split('.')[0]))
folder = inp_file.split('/')[1].split('.')[0]

def txt2QR(i):
    file = f'vicks/output/{i}'

    try:
        os.mkdir(f"output/{folder}")
    except Exception as e:
        pass 

    with open(file, 'rb') as f:
        data = f.read()
        # print(data)

    try:
        img.add_data(data)
        img.make(fit=True)
        image = img.make_image(fill_color="black", back_color="white")
        
        photo = f"output/{folder}/{i.split('.')[0]}.jpg"
        image.save(photo)

    except Exception as e:
        # print(e)
        pass

def frame2video(path = f"output/{folder}"):
	mean_height = 0
	mean_width = 0

	num_of_images = len(os.listdir(path))
	print(f'num_of_images = {num_of_images}')

	for file in os.listdir(path):
		im = Image.open(os.path.join(path, file))
		width, height = im.size
		mean_width += width
		mean_height += height

	mean_width = int(mean_width / num_of_images)
	mean_height = int(mean_height / num_of_images)

	for file in os.listdir(path):
		if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
			im = Image.open(os.path.join(path, file))

			width, height = im.size
			imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
			imResize.save(os.path.join(path, file), 'JPEG', quality = 95)
			print(im.filename.split('\\')[-1], " is resized")

	def generate_video():
		image_folder = path
		video_name = 'mygeneratedvideo.avi'
		
		images = [img for img in os.listdir(image_folder)
				if img.endswith(".jpg") or
					img.endswith(".jpeg") or
					img.endswith("png")]
		
		frame = cv2.imread(os.path.join(image_folder, images[0]))
		height, width, layers = frame.shape
		video = cv2.VideoWriter(os.path.join('output', video_name), 0, 1, (width, height))

		for image in images:
			print('Writing for ', image)
			video.write(cv2.imread(os.path.join(image_folder, image)))
		
		cv2.destroyAllWindows()
		video.release()

	generate_video()


def framerate():
	in_loc = 'output/mygeneratedvideo.avi'
	out_loc = 'output/final.mp4'

	clip = VideoFileClip(in_loc)
	clip = clip.set_fps(clip.fps * 30)
	final = clip.fx(vfx.speedx, 30)

	audioclip = AudioFileClip("vicks/TV.mp4")
	videoclip = final.set_audio(audioclip)
	videoclip.write_videofile(out_loc)
        
for i in dirFiles[:]:
    print(i)
    txt2QR(i)

frame2video()
framerate()
