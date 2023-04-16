
import zipfile

def compress_zip(file):
    print('Zipping...')
    with zipfile.ZipFile('output.zip', 'w', zipfile.ZIP_DEFLATED) as f:
        f.write(file)
    print('Zipped.')

def decompress_unzip():
    print('Unzipping...')
    with zipfile.ZipFile('output.zip', 'r') as f:
        f.extractall('.')
    print('Unzipped.')

# file = 'smile.gif.avi'

# compress_zip(file)
# decompress_unzip()
