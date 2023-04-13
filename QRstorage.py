
import qrcode, os
from PIL import Image

img = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=1,
)

with open('CSV.txt', 'r') as f:
    data = f.read()

img.add_data(data)
img.make(fit=True)

photo = 'QR.jpg'
img = img.make_image(fill_color="black", 
                     back_color="white")
img.save(photo)

os.startfile(photo)
print(img)
