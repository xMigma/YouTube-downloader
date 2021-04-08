import moviepy.editor as mp
import time
import os

def convertir_mp3(video):
    clip = mp.VideoFileClip(video)
    clip.audio.write_audiofile(video[:-4] + ".mp3")
    clip.close()
    os.remove(video)   