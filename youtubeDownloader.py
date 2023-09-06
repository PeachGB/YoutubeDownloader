#! /usr/bin/python
"""this line ↑↑↑ indicates the shell that you're gonna
open this program using python. If you dont know where python is in your
system you can run "which python" or "which python3" in the cli
and it will tell you, paste the output on the #!


you would want to edit the .bashrc file in the home folder to create an alias for this program

you can do this by simply put
Alias ytd='[PUT HERE THE PATH OF THE PROGRAM]'
"ytd" will be the name of the command you gotta put in the cli for this init.
You can put whatever name you want for the command
 """
from pytube import YouTube

#this is where the video will save change the path for your user
SAVE_PATH = "/home/arian/Videos/ytD"


Link = input("paste url ")

try:
    yt = YouTube(Link)
except:
    print("not a valid url")
mp4Files = yt.streams.filter(progressive=True)

for file in mp4Files:
    print(file)


itag = input("select itag to download: ")
fn = input("download as?: ")
print("DOWNLOADING... PLEASE WAIT")

stream = yt.streams.get_by_itag(itag)
stream.download(output_path = SAVE_PATH,filename= fn +'.mp4')
print("COMPLETE")
