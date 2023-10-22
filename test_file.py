from noris_speak import Speak
from pygame import mixer
import threading
import random
import time
PLAYLIST_URL = 'Rap Songs New'
APPROX_TIME_TO_RUN_LOOP = 0.001
ISPAUSED = False


def get_song_lenght(song_file:str) -> int:
        print(song_file) #Rap Songs New\Venom - Music From The Motion Picture.mp3
        from mutagen.mp3 import MP3
        audio = MP3(song_file)
        return audio.info.length

def play_music(text):
    from os import listdir
    from os.path import isfile, join
    PLAYLIST_URL = 'Rap Songs New'
    music_files = [f for f in listdir(PLAYLIST_URL) if isfile(join(PLAYLIST_URL, f))]
#    print(music_files)

    def play():
        random.shuffle(music_files)
        for music_file in music_files:
            mixer.init()
            mixer.music.load('Rap Songs New/'+music_file)
            mixer.music.set_volume(0.7)
            mixer.music.play()
            _ = True
            while _:
                status = mixer.music.get_busy()
                if status == True:
                    time.sleep(APPROX_TIME_TO_RUN_LOOP)
                elif status == False and ISPAUSED == False:
                    print('FALSEEEEE')
                    _ = False

    def pause():
        mixer.music.pause()
        global ISPAUSED
        ISPAUSED = True

    def resume():
        mixer.music.unpause()
        time.sleep(100)
        global ISPAUSED
        ISPAUSED = False

    if 'play' in text:
        play()

    if 'pause' in text:
        pause()
    
    if 'resume' in text:
        resume()


while True:
    text = input('YOU:: ')
    if 'music' in text:
        thread_music = threading.Thread(target=play_music, args=(text,))
        thread_music.start()
        