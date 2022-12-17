from pickle import TRUE
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

reader = SimpleMFRC522()

DEVICE_ID= ""
CLIENT_ID= ""
CLIENT_SECRET= ""

#Spotify Authentication
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
#                                                client_secret=CLIENT_SECRET,
#                                                redirect_uri="http://google.com/",
#                                                scope=" user-modify-playback-state user-library-read playlist-read-private user-read-playback-state user-read-currently-playing",
#                                                open_browser=False)) # open_browser = false, da pi zero zu langsam ist um den Browser zu authentication zu öffenen
#
#change volume
#sp.volume(volume_percent=50)

while(True):
    #Spotify Authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://google.com/",
                                                scope=" user-modify-playback-state user-library-read playlist-read-private user-read-playback-state user-read-currently-playing",
                                                open_browser=False)) # open_browser = false, da pi zero zu langsam ist um den Browser zu authentication zu öffenen

    try:
        print("Wait for you to scan a RFID card/tag")
        id = reader.read()[0]
        print("The ID for the Card/Tag is: ", id)
        #sp.transfer_playback(device_id=DEVICE_ID, force_play=True)
        #Playlist: Habibi Funk
        if id == 506988078465:
            sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:04KTRZz1h4AMUK8VQrJuPl')     #Playlist: HabibiFunk
            #for a song
            #sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3rh495Z2rIRwD316blea4f'])
            #for a album
            #sp.start_playback(context_uri='spotify:album:19Y5unyuRZrnaKxRLzbQBs')
	        #sp.volume(volume_percent=70)
            sp.shuffle(TRUE)
            sleep(3)
        #Playlist: ...
        elif id == 290216909070:
            
            sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:3EqH4zb1aPbxV2SBLdA3x6')     #Playlist: ...
            #sp.volume(volume_percent=70)
            sp.shuffle(TRUE)
            sleep(3)
         #Playlist: Hip Hop Paraguay
        elif id == 84023154993:
            
            sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:3djAhflwauqATzX5Vc1HBT')     #Playlist: Hip Hop Paraguay
            #sp.volume(volume_percent=70)
            sp.shuffle(TRUE)
            sleep(3)
         #Playlist: Panama.
        elif id == 976034568459:
            
            sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:2VOnaoA9SH1s1h20Qw0Ulc')     #Playlist: Pananma
            #sp.volume(volume_percent=70)
            sp.shuffle(TRUE)
            sleep(3)
         #Playlist: elektrisch Bolivien
        elif id == 1047120222621:
            
            sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:3wgl3gwrKBoYe3PcowNig0')     #Playlist: elektrisch Bolivien
            #sp.volume(volume_percent=70)
            sp.shuffle(TRUE)
            sleep(3)
        #Playlist: nightshift.
        elif id == 291005765968:
            
            sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:2Tbl4ISlhsKIRAxBknFgDJ')     #Playlist: nightshift.
            #sp.volume(volume_percent=70)
            sp.shuffle(TRUE)
            sleep(3)
        # pausiert den     
        elif id == 702348433799:
            sp.pause_playback()
            sleep(3)
        #plays the current track
        elif id == 976086079866:
            sp.start_playback()
            sleep()
 
    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
        #...
        #https://open.spotify.com/playlist/3EqH4zb1aPbxV2SBLdA3x6?si=e0becd0960154535
        # Habibi Funk
        #https://open.spotify.com/playlist/04KTRZz1h4AMUK8VQrJuPl?si=6a9b7c3689444731
        #Hip Hop Paraguay
        #https://open.spotify.com/playlist/3djAhflwauqATzX5Vc1HBT?si=c58784e2482d4634
        #Panama.
        #https://open.spotify.com/playlist/2VOnaoA9SH1s1h20Qw0Ulc?si=034c592c217b43d8
        #elektrisch Bolivien
        #https://open.spotify.com/playlist/3wgl3gwrKBoYe3PcowNig0?si=41253f4308814128
        #nightshift.
        #https://open.spotify.com/playlist/2Tbl4ISlhsKIRAxBknFgDJ?si=7dda5961a5ef483c
        #Album: 5 Dimension
        #https://open.spotify.com/album/19Y5unyuRZrnaKxRLzbQBs?si=cVa93AhDTbaByewDvvdPrA
