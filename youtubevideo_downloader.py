import os
import time
from pytube import YouTube

def clear():
    name = os.name
    if name == 'nt':
        _ = os.system('cls')
    else:
        os.system('clear')


clear()
x="""\33[31m\n

 Y   Y  OOO  U   U TTTTTT U   U BBBB  EEEE   V     V III DDD  EEEE  OOO      DDD   OOO  W     W N   N L     OOO  AA  DDD  EEEE RRRR 
  Y Y  O   O U   U   TT   U   U B   B E      V     V  I  D  D E    O   O     D  D O   O W     W NN  N L    O   OA  A D  D E    R   R
   Y   O   O U   U   TT   U   U BBBB  EEE     V   V   I  D  D EEE  O   O     D  D O   O W  W  W N N N L    O   OAAAA D  D EEE  RRRR 
   Y   O   O U   U   TT   U   U B   B E        V V    I  D  D E    O   O     D  D O   O  W W W  N  NN L    O   OA  A D  D E    R R  
   Y    OOO   UUU    TT    UUU  BBBB  EEEE      V    III DDD  EEEE  OOO      DDD   OOO    W W   N   N LLLL  OOO A  A DDD  EEEE R  RR                                                                                                                                   
"""
y = 0
while y <= len(x):
    os.system('clear')
    os.system('cls')
    print(x[:y])
    time.sleep(0)
    y = y+1
link = input("Enter the link: ")
yt= YouTube(link)
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length,"seconds")
print("Description: ", yt.description)
print()
print("Rating: ", yt.rating)

print(yt.streams)

k=input("Does you want only audio Press(a),For only video Press(v), for both Press(b): ")
if k == 'a':
   print(yt.streams.filter(only_audio=True))
   l=input("\33[34m\nEnter Resolution itag from above:- ")
   ys=yt.streams.get_by_itag(l)
   ys.download()
elif k == 'v':
    print(yt.streams.filter(only_video=True))
    l=input("Enter Resolution itag from above:- ")
    ys=yt.streams.get_by_itag(l)
    ys.download()
elif k == 'b':
    print(yt.streams.filter(progressive=True))
    l=input("Enter Resolution itag from above:- ")
    ys=yt.streams.get_by_itag(l)
    ys.download()
print("Downloaded File Stores In Same Folder....")
