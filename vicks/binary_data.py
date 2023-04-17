
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.all as vfx
import os, zipfile


def file_to_binary_string(file_path):
    with open(file_path, 'rb') as file:
        binary_code = file.read()
        byte_list = (format(byte, '08b') for byte in binary_code)
        binary_string = ''.join(byte_list)
    return binary_string


def binary_string_to_file(binary_string, file_path):
    with open(file_path, 'wb') as file:
        bytes_list = [int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)]
        bytes_arr = bytearray(bytes_list)
        file.write(bytes_arr)


def insert_newlines(string, every=8*20):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))


def save_binary(in_directory, out_directory, filename):
    file_path = os.path.join(in_directory, filename)

    if os.path.isfile(file_path):
        binary_string = file_to_binary_string(file_path)
        binary_string = insert_newlines(binary_string)
        # print(binary_string)

        file_path = os.path.join(out_directory, 'UNIQUE.txt')
        with open(file_path, 'w') as f:
            f.write(binary_string)

# save_binary(in_directory, out_directory, filename)


def write_all(in_directory, out_directory, filename):
    for filename in os.listdir(in_directory):
        save_binary(in_directory, out_directory, filename)


def revert_back(in_directory, out_directory, filename):
    file_in = os.path.join(in_directory, filename)
    file_out = os.path.join(out_directory, filename)

    with open(file_in, 'r') as f:
        binary_string = f.read()

        binary_string = ''.join(binary_string.split('\n'))
        # print(binary_string)
    binary_string_to_file(binary_string, file_out)

# revert_back(in_directory, out_directory, filename)


def compress_zip(file):
    print('>>> Zipping...')
    with zipfile.ZipFile(f'{file}.zip', 'w', zipfile.ZIP_DEFLATED) as f:
        f.write(file)
    print('>>> Zipped')


def decompress_unzip():
    print('>>> Unzipping...')
    with zipfile.ZipFile('output.zip', 'r') as f:
        f.extractall('.')
    print('>>> Unzipped.')

# decompress_unzip()


def framerate(in_loc, out_loc):
    videoclip = VideoFileClip(in_loc)
    # videoclip = videoclip.set_fps(videoclip.fps * 1)
    videoclip = videoclip.fx(vfx.speedx, 5)
    videoclip.write_videofile(out_loc)

# framerate(in_loc, out_loc)
