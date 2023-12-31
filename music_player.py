from noris_speak import Speak

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

def play(playlist_url:str, is_playlist:bool):
    def get_songs_in_playlist(playlist_url:str) -> list:
        from os import listdir
        from os.path import isfile, join
        music_files = [f for f in listdir(playlist_url) if isfile(join(playlist_url, f))] #gets the files from the url
        return music_files
    
    def get_song_lenght(song_file:str) -> int:
        print(song_file) #Rap Songs New\Venom - Music From The Motion Picture.mp3
        from mutagen.mp3 import MP3
        audio = MP3(song_file)
        return audio.info.length

    def play_current_song(filename:str, volume:float):
        from pygame import mixer
        mixer.init() 
  
        # Loading the song 
        mixer.music.load(filename=filename)
        
        # Setting the volume 
        mixer.music.set_volume(volume)
        # Start playing the song 
        mixer.music.play() 


    if is_playlist:
        import time
        import random
        songs_in_playlist = get_songs_in_playlist(playlist_url)
        random.shuffle(songs_in_playlist)
        for song in songs_in_playlist:
            print(song) #PRINT SONGS
            filename = 'Rap Songs New/'+song
            play_current_song(filename=filename, volume=0.3)
            lenght_song = get_song_lenght(filename)
            time.sleep(lenght_song)
        
"""
def check_if_downloaded():
    songs_spotify = get_songs_in_spotify()
    songs_downloaded = get_songs_downloaded()
    for song in songs_spotify:
        if song not in songs_downloaded:
            download_song(song)
"""

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
            play(PLAYLIST_URL, True)
    IS_PLAYING = False
    return 
    
def pause_music():
    from pygame import mixer
    print('pausing')
    mixer.music.pause()

def unpause_muisc():
    from pygame import mixer
    print('unpausing')
    mixer.music.unpause()

#play_music('play music')