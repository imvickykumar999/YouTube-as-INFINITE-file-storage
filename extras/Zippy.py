
import zipfile

def compress_zip():
    with zipfile.ZipFile('output.zip', 'w', zipfile.ZIP_DEFLATED) as f:
        f.write('Bed Bugs - Coyote Hearing.mp3')

def decompress_unzip():
    with zipfile.ZipFile('output.zip', 'r') as f:
        f.extractall('.')

compress_zip()
decompress_unzip()
