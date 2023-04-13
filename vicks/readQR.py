
# pip install pyzbar

from pyzbar.pyzbar import decode
from PIL import Image

file = "input/1.jpg"
out = decode(Image.open(file))

out = out[0].data.decode('utf-8')
print(out)



# OUTPUT
'''

# https://colab.research.google.com/drive/1QBMU9-v5jowlzg3fncjlrUKirWTHtKjq#scrollTo=es8m5ragAPDT



'''
