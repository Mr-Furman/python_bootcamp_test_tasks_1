import requests
import os, sys
from moviepy.editor import *


def tiktok_to_gif():
    """convert TikTok to gif"""

    URL = "https://v16m-webapp.tiktokcdn-us.com/a6e3b7e6a064bc43da3a39ab93460ef8/62e921d5/video/tos/useast5/tos-useast5-ve-0068c003-tx/41b44c2a3cc840929f658665d57979d1/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1150&bt=575&cs=0&ds=3&ft=ebtHKH-qMyq8ZwkJKwe2NoTcfl7Gb&mime_type=video_mp4&qs=0&rc=aTozOTNmZmg5MzpnOzo1ZUBpM3g6OmQ6ZmhvZTMzZzczNEAwLjRiMDZhNmMxLmJfMTYzYSNqczAycjRnYmZgLS1kMS9zcw%3D%3D&l=20220802070706CBA8CD072C869B2562D9"
    response = requests.get(URL)
    open("tiktoc.mp4", "wb").write(response.content)
    clip = (VideoFileClip("tiktoc2.mp4").speedx(10).resize(0.3))
    file = "tiktoc.gif"
    clip.write_gif(file)
    print("Done.")
    directory = os.getcwd() + "\\" + file
    return print(directory)


tiktok_to_gif()
