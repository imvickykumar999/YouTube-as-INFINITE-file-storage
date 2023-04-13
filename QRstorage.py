
from vicks import split_file as sf
import qrcode, os, cv2
from PIL import Image

Image.MAX_IMAGE_PIXELS = 933120000
# inp_file = 'input/really_big_file.txt'
inp_file = input('Enter file name from input folder : ')

try:
	os.mkdir('vicks/output')
except Exception as e:
	pass

try:
	os.mkdir("vicks/video")
except Exception as e:
	pass 

folder = inp_file.split('/')[1].split('.')[0]
sf.split(inp_file)

dirFiles = os.listdir('vicks/output')
dirFiles.sort(key=lambda f: int(f.split('.')[0]))

def txt2QR(i):
	img = qrcode.QRCode(
		version=2,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=100,
		border=5,
	)
	
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

	dirfiles = os.listdir(path)
	dirfiles.sort(key=lambda f: int(f.split('.')[0]))

	num_of_images = len(dirfiles)
	print(f'num_of_images = {num_of_images}')

	for file in dirfiles:
		im = Image.open(os.path.join(path, file))
		width, height = im.size
		mean_width += width
		mean_height += height

	mean_width = int(mean_width / num_of_images)
	mean_height = int(mean_height / num_of_images)

	for file in dirfiles:
		if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
			im = Image.open(os.path.join(path, file))

			width, height = im.size
			imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
			imResize.save(os.path.join(path, file), 'JPEG', quality = 95)
			print(im.filename.split('\\')[-1], " is resized")

	video_name = f'video/{folder}.avi'
	images = [
		img for img in dirfiles
		if img.endswith(".jpg") or
		img.endswith(".jpeg") or
		img.endswith("png")
	]
	
	frame = cv2.imread(os.path.join(path, images[0]))
	height, width, layers = frame.shape
	video = cv2.VideoWriter(os.path.join('vicks', video_name), 0, 1, (width, height))

	for image in images:
		print('Writing for ', image)
		video.write(cv2.imread(os.path.join(path, image)))
	
	cv2.destroyAllWindows()
	video.release()

if __name__=='__main__':
	for i in dirFiles[:10]:
		print(i)
		txt2QR(i)

	frame2video()
