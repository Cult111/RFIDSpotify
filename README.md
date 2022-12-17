# RFIDSpotify
What to install:

Update Pi:
sudo apt-get update
sudo apt-get upgrade


PiP3:
sudo apt-get -y install python3-pip

Enable SPI:
sudo raspi-config
-> Interface -> SPI


RFID card reader:
sudo pip3 install spidev
sudo pip3 install mfrc522

Git:
sudo apt install git

Soundcard:
git clone https://github.com/waveshare/WM8960-Audio-HAT
cd WM8960-Audio-HAT
sudo ./install.sh
sudo reboot

sudo nano /usr/share/alsa/alsa.conf 

defaults.ctl.card 0 -> defaults.ctl.card 1
defaults.pcm.card 0 -> defaults.pcm.card 1

sudo alsamixer -> change volume


Raspotify for raspberry pi zero:
sudo apt-get -y install curl && curl -O -sL https://github.com/dtcooper/raspotify/releases/download/0.31.8.1/raspotify_0.31.8.1.librespot.v0.3.1-54-gf4be9bb_armhf.deb

sudo apt install ./raspotify_0.31.8.1.librespot.v0.3.1-54-gf4be9bb_armhf.deb


Spotipy
pip install spotipy --upgrade



Add Script to Corntab for autostart

sudo crontab -e

#letzte Zeile
@reboot cd /home/pi/RFIDSpotify && python SpotifyRFIDPlayer.py >/tmp/SpotifyPla>
