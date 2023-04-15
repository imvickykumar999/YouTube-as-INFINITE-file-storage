
from itertools import zip_longest
from pytube import YouTube
import re, requests

def split(file = 'input/really_big_file.txt'):
    n = 3

    def grouper(n, iterable, fillvalue=None):
        args = [iter(iterable)] * n
        return zip_longest(fillvalue=fillvalue, *args)

    with open(file) as f:
        for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
            with open(f'vicks/output/{i}.txt', 'w') as fout:
                fout.writelines(g)

def ytvideo(link):
    # link = input("Enter link here: ")
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()

    path_to_download_folder = 'video'
    filename = yt.title.replace(' ', '')
    filename = re.sub('[^A-Za-z0-9]+', '', filename)

    video.download(path_to_download_folder.replace(' ',''), filename=f'{filename}.mp4')
    return f'{filename}.mp4'

def instavideo():
    req = requests.get('https://www.instagram.com/p/CqTC9d3vYlX/?__a=1&__d=1')
    js = req.json()
    x = js['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][0]['node']['video_url']
