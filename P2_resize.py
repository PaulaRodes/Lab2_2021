import os

#  resize to 720p
os.system("ffmpeg -i bbb_cut.mp4 -vf scale=1280:720 bbb_720p.mp4".format("mp4"))
#  resize to 480p
os.system("ffmpeg -i bbb_cut.mp4 -vf scale=720:480 bbb_480p.mp4".format("mp4"))
#  resize to 360x240
os.system("ffmpeg -i bbb_cut.mp4 -vf scale=360:240 bbb_360x240.mp4".format("mp4"))
#  resize to 160x120
os.system("ffmpeg -i bbb_cut.mp4 -vf scale=160:120 bbb_160x120.mp4".format("mp4"))
