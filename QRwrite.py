
from vicks import binary_data as bd
from vicks import split_file as sf

import qrcode, os, cv2, shutil
from PIL import Image
import urllib.request


try:
	os.mkdir('vicks/output')
except Exception as e:
	pass

try:
	os.mkdir('output')
except Exception as e:
	pass

try:
	os.mkdir("vicks/video")
except Exception as e:
	pass 


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

	try:
		with open(file, 'r', encoding="utf-8") as f:
			data = f.read()
	except:
		with open('input/' + i, 'rb') as f:
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


def frame2video(path):
	mean_height = 0
	mean_width = 0

	dirfiles = os.listdir(path)
	dirfiles.sort(key=lambda f: int(f.split('.')[0]))

	num_of_images = len(dirfiles)
	print(f'\nNumber of Images = {num_of_images}')

	for file in dirfiles:
		im = Image.open(os.path.join(path, file))
		width, height = im.size
		mean_width += width
		mean_height += height

	mean_width = int(mean_width / num_of_images)
	mean_height = int(mean_height / num_of_images)
	
	video_name = f'video/{folder}.avi'
	images = [
		img for img in dirfiles
		if img.endswith(".jpg") or
		img.endswith(".jpeg") or
		img.endswith("png")
	]
	
	frame = cv2.imread(os.path.join(path, images[0]))
	height, width, layers = frame.shape

	ospath = os.path.join('vicks', video_name)
	video = cv2.VideoWriter(ospath, 0, 1, (width, height))

	print()
	for image in images:
		print('Writing for ', image)
		video.write(cv2.imread(os.path.join(path, image)))
	
	bd.compress_zip(ospath)
	# print(ospath)
	# bd.framerate(ospath, ospath + '.mp4')

	cv2.destroyAllWindows()
	video.release()


if __name__=='__main__':
	Image.MAX_IMAGE_PIXELS = 933120000

	# filename = 'input/really_big_file.txt'
	filename = input('Enter `URL` or file `name` from input folder : ')

	try:
		file = f'{os.path.basename(filename)}'
		filepath = os.path.join('input', file)
		urllib.request.urlretrieve(filename, filepath)
	except:
		file = filename

	out_directory = in_directory = 'input/'
	inp_file = in_directory + file

	folder = inp_file.split('/')[1]
	bd.save_binary(in_directory, out_directory, file)
	inp_file = in_directory + 'UNIQUE.txt'

	try:
		sf.split(inp_file)
		dirFiles = os.listdir('vicks/output')
		dirFiles.sort(key=lambda f: int(f.split('.')[0]))

		for i in dirFiles[:]:
			print(i)
			try:
				txt2QR(i)
			except:
				pass
		frame2video(f"output/{folder}")
		
	except Exception as e:
		path = '1.jpg'
		print(e)
		txt2QR(path)


input('\n\tPress any key to delete splitter text folder')
shutil.rmtree('vicks/output')
