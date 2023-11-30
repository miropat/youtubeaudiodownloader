from pytube import YouTube
from moviepy.editor import *



video_url = input("Please enter the video URL: ")
yt = YouTube(video_url,
            use_oauth=False,
            allow_oauth_cache=True)



#print("View: ", yt.views)

video = yt.streams.filter(only_audio=True, file_extension="mp4").first()


video.download()


#convert audio

original_filename = video.default_filename
new_filename = original_filename.replace(".mp4", ".mp3")
import os
os.rename(original_filename, new_filename)

print("Title: ", yt.title + " has been downloaded and converted")

