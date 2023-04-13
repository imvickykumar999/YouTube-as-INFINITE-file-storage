
from vicks import split_file as sf
import qrcode, os

img = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=5,
)

inp_file = 'input/really_big_file.txt'
sf.split(inp_file)

dirFiles = os.listdir('vicks/output')
dirFiles.sort(key=lambda f: int(f.split('.')[0]))

def txt2QR(i):
    file = f'vicks/output/{i}'
    folder = inp_file.split('/')[1].split('.')[0]

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
        
        photo = f"output/{folder}/{i}.jpg"
        image.save(photo)

    except Exception as e:
        print(e)
        pass

for i in dirFiles[:]:
    txt2QR(i)
