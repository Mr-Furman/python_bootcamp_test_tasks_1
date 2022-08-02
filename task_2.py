import requests
import os, sys
from moviepy.editor import *


def tiktok_to_gif():
    """convert TikTok to gif"""

    URL = input('Type your URL ')
    response = requests.get(URL)
    open("tiktoc.mp4", "wb").write(response.content)
    clip = (VideoFileClip("tiktoc2.mp4").speedx(10).resize(0.3))
    file = "tiktoc.gif"
    clip.write_gif(file)
    print("Done.")
    directory = os.getcwd() + "\\" + file
    return print(directory)


tiktok_to_gif()
