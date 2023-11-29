import yt_dlp

# Enter Youtube video url for the download 

url = input("Please Enter preferred youtube video url : ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded Successfully, thank you !!")