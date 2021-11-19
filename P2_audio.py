import os

#  audio to mono and change the audio codec
os.system("ffmpeg -i bbb_cut.mp4 -ac 1 bbb_mono.flac".format("mp4"))