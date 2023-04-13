
import qrcode
import os

img = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=2,
)

file = 'input//keywords.csv'
name = file.split('//')[1].split('.')[0]

try:
    os.mkdir(f'output//{name}')
except Exception as e:
    pass 

with open(file, 'rb') as f:
    data = f.read()

img.add_data(data)
img.make(fit=True)
img = img.make_image(fill_color="black", back_color="white")

photo = f'output//{name}//{name}.jpg'
img.save(photo)
