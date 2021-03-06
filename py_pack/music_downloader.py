from pytube import YouTube
import os
import requests
from pytube.cli import on_progress

username = os.environ.get("USERPROFILE")

def play(topic):
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        raise Exception("No video found.")
    return "https://www.youtube.com"+lst[count-5]
def rename(direc):
    direc = direc.replace('/', '\\')
    source = direc
    direc = direc.replace(".mp4", ".mp3")
    path = direc
    os.rename(source, path)
def download(topic, asking):
    "Topic: Video URl, Asking: Audio Video"
    if str(topic).startswith('https://www.youtube.com/'):
        url = topic
    else:
        url = play(topic)
    ytd = YouTube(url)
    if asking == 'audio':
        title = ytd.title
        print("Downloading Audio {}.mp3".format(title))
        try:
            cb = ytd.streams.get_audio_only().download(f"{username}/Music")
        except ConnectionResetError:
            print("Audio cannot be downloaded=> Connection has been reset")
        ytd.register_on_complete_callback(rename(cb))
    elif asking == 'video':
        print("Downloading Video {}.mp4".format(ytd.title))
        try:
            ytd.streams.get_highest_resolution().download(f"{username}/Videos")
        except:
            print("Video cannot be downloaded=>Connection reset")
    else:
        print("Invalid Argument")
    print('Download Completed')
    return True
