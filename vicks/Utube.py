from pytube import YouTube
import os
from pathlib import Path

link = input("Enter link here: ")
url = YouTube(link)

print("downloading....")
video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
# print(path_to_download_folder)

video.download(path_to_download_folder)
print("Downloaded! :)")
