
# pip install pyzbar

from pyzbar.pyzbar import decode
from PIL import Image

file = "input/1.jpg"
# Extract each frame of any video
# https://github.com/imvickykumar999/Video-Colorization/blob/b377fcacc84d39ab9ea151b2642866c0ea69496b/video_colorization.py#L30

out = decode(Image.open(file))

out = out[0].data.decode('utf-8')
print(out)



# OUTPUT
'''

# https://colab.research.google.com/drive/1QBMU9-v5jowlzg3fncjlrUKirWTHtKjq#scrollTo=es8m5ragAPDT



'''
