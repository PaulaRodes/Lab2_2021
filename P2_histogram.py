import os

#  new video with YUV histogram overlay
os.system("ffmpeg -y -report -i bbb_cut.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay bbb_hist.mp4")
