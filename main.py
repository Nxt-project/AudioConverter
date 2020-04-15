from moviepy.editor import *
import os
import sys

if __name__ == '__main__':
    if not os.path.exists('videos'):
        os.mkdir('videos')
    if not os.path.exists('audios'):
        os.mkdir('audios')
    dir = os.listdir('videos')
    # Check is the videos directory empty
    if not dir:
        print("Please put videos in the 'videos' directory for a convert!")
        sys.exit(0)
    for file in dir:
        video = VideoFileClip(os.path.join('videos/', file))
        video.audio.write_audiofile(os.path.join('audios', file[:-4] + '.mp3'))