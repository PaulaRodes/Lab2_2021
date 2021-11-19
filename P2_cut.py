import os

#  cut a 12 second clip
os.system("ffmpeg -ss 00:00:00 -i bbb_original.mp4 -c copy -t 00:00:12.0 bbb_cut.mp4".format("mp4"))
