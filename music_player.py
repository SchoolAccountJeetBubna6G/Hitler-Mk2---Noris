from noris_speak import Speak
from pygame import mixer
import random
#STEPS TO GET MUSIC
"""
PRE-SETUP
1) Start program
2) Get songs in spotify playlists
3) Compare with the downloaded songs
4) If songs are there in spotify, which are no there in downloaded, download songs
6) Get the playlist that needs to be played - if none provided, play rap songs new
"""
#STEP TO DOWNLOAD MUSIC
"""
1) Use YT api, for the videos not in downloaded set, to get their URL
2) Use pytube to download videos
"""
#MAIN LOOP IF THIS IS CALLED
"""
1) Get the current playing song
2) If 'play' play, if 'stop' stop
3) If 'play' followed by a name (Determi`ne by some algorithm), play name
"""
CLIENT_ID = 'e20c25956b1e48228ddc9309f3e4d6b2'
CLIENT_SECRET = '27b5ee6d34d146e4b62ca13c9be25d42'
AUTOHORIZE_ENDPOINT = 'https://accounts.spotify.com/authorize'
REDIRECT_URL = "https://www.google.co.in/"
SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-library-modify user-library-read user-read-email user-read-private user-read-playback-state user-modify-playback-state"
PLAYLIST_URL = 'Rap Songs New'

PLAY_WORDS_NOT_REQ = ['play','blast'] #Words that if present, good, but if not, then its ok
REQUIRED_WORDS = ['music', 'song']
IS_PLAYING = False
IS_PAUSED = False

"""
def get_songs_in_spotify() -> list:
    
    def get_current_url(url:str) -> str:
        pass

    def get_code_spotify() -> str:
        import webbrowser
        from urllib.parse import urlencode

        auth_headers = {
            "client_id": CLIENT_ID,
            "response_type": "code",
            "redirect_uri": REDIRECT_URL,
            "scope": SCOPE
        }

        #webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
        code_url = get_current_url("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
        #TO FINSIH NOT COMPLETE ------------------------  TO FINISH NOT COMPLETE        
    def get_access_code(code:str) -> str:
        pass

    code = get_code_spotify()
    access_code = get_access_code(code)
"""


def get_songs_downloaded() -> list:
    pass

def download_song(name:str):
    pass

def get_current_playing_song() -> str:
    pass


def get_songs_in_playlist(playlist_url:str) -> list:
        from os import listdir
        from os.path import isfile, join
        music_files = [f for f in listdir(playlist_url) if isfile(join(playlist_url, f))] #gets the files from the url
        return music_files


        
"""
def check_if_downloaded():
    songs_spotify = get_songs_in_spotify()
    songs_downloaded = get_songs_downloaded()
    for song in songs_spotify:
        if song not in songs_downloaded:
            download_song(song)
"""

def play(music_files:list, APPROX_TIME_TO_RUN_LOOP:float):
        import time
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
                elif status == False and IS_PAUSED == False:
                    print('FALSEEEEE')
                    _ = False

def play_music(text:str):
    #PRE SETUP
    #check_if_downloaded()
    
    for word in REQUIRED_WORDS:
        if word in text:
            Speak('Sure! Playing music!')
            print('Playing, music!')
            #print(IS_PLAYING)
            global IS_PLAYING
            IS_PLAYING = True
            play(get_songs_in_playlist(PLAYLIST_URL), 0.001)
    IS_PLAYING = False
    return 
    
def pause_music():
    Speak('pausing')
    mixer.music.pause()
    global IS_PAUSED
    IS_PAUSED = True

def unpause_muisc():
    Speak('unpausing')
    mixer.music.unpause()
    global IS_PAUSED
    IS_PAUSED = True

#play_music('play music')