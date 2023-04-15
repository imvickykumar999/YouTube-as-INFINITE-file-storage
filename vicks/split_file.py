
from itertools import zip_longest
import urllib.request, time
from pytube import YouTube
import re, requests, os


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
    # filename = f'{time.time()}'

    filename = re.sub('[^A-Za-z0-9]+', '', filename)
    video.download(path_to_download_folder.replace(' ',''), filename=f'{filename}.mp4')
    return f'{filename}.mp4'


def uploadonYT():
    from simple_youtube_api.Channel import Channel
    from simple_youtube_api.LocalVideo import LocalVideo

    # loggin into the channel
    channel = Channel()
    channel.login("client_secret.json", "credentials.storage")

    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path="test_vid.mp4")

    # setting snippet
    video.set_title("My Title")
    video.set_description("This is a description")
    video.set_tags(["this", "tag"])
    video.set_category("gaming")
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("private")
    video.set_public_stats_viewable(True)

    # setting thumbnail
    video.set_thumbnail_path('test_thumb.png')

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.id)
    print(video)

    # liking video
    video.like()


def getname(url):
    """Split the URL from the username"""
    url = list(url.split('/'))

    if len(url) == 1:
        url = url[0]
        itis = 'user'

        if len(url) == 11 and url[0] == 'C':
            itis = 'reels'
    else:
        if url[3] in ['reels', 'reel', 'p']:
            url = url[4]
            itis = 'reels'
        else:
            url = url[3]
            itis = 'user'
    return url, itis


def instavideo(url = 'ClwrpW1BB-R'):
    url = getname(url)[0]
    link = f'https://www.instagram.com/p/{url}/?&__a=1&__d=1'

    user = requests.get(link)
    a = user.json()
    x = a['graphql']['shortcode_media']

    if x['is_video']:
        b = [x['video_url']]
        c = [x['display_url']]
    else:

        try:
            d,e = [],[]
            for i in x['edge_sidecar_to_children']['edges']:
                y = i['node']

                try:
                    b = y['video_url']
                    c = y['display_resources'][-1]['src']
                except:
                    b = "Click Below Link to Download Photo" 
                    c = y['display_url']

                d.append(b)
                e.append(c)
            b,c = d,e

        except:
            b = ["Click Below Link to Download Photo"] 
            c = [x['display_url']]
    
    # x = f'{os.path.basename(c[0])}'
    x = f'{time.time()}'

    x = re.sub('[^A-Za-z0-9]+', '', x)
    a = os.path.join('video', x+'.mp4')

    urllib.request.urlretrieve(b[0], a)
    return x+'.mp4'
