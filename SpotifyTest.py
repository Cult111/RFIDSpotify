import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID= ""
CLIENT_ID= ""
CLIENT_SECRET= ""

 #Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://google.com/",
                                                scope=" user-modify-playback-state user-library-read playlist-read-private user-read-playback-state user-read-currently-playing",
                                                open_browser=False)) # open_browser = false, da pi zero zu langsam ist um den Browser zu authentication zu öffenen

# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(DEVICE_ID, force_play=True)

sp.shuffle(state=True)

sp.volume(volume_percent=100)

# Play the spotify track at URI with ID 59EiGiciwk8QMrYkrHxIUd
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:59EiGiciwk8QMrYkrHxIUd'])

def playpause():
    global playstate
    if playstate is True:  # dont know how to read from api :(
        print("Pausing...")
        playstate = False
        sp.pause_playback(device_id=DEVICE_ID)
    else:
        print("Resuming...")
        playstate = True
        sp.start_playback(device_id=DEVICE_ID)
