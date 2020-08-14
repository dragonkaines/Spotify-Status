import rumps
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Spotipy - Authentication: 
cid = ''
csecret = ''
username = ''
scope = 'streaming user-read-currently-playing user-read-playback-state'

redirect_uri = 'http://localhost:8888/callback/'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=csecret)
token = util.prompt_for_user_token(username, scope, cid, csecret, redirect_uri)
sp = spotipy.Spotify(auth=token)

# The Status Bar Work: 
class StatusBar(rumps.App):
    def __init__(self):
        super(StatusBar, self).__init__("Spotify Status")
        self.menu = ["Previous Song","Next Song", "Current Song"]

    @rumps.clicked("Current Song")
    def current(self, _):
        currently_playing = sp.currently_playing()
        song_name = currently_playing['item']['name']
        song_artist = currently_playing['item']['artists'][0]['name']
        rumps.alert("Currently Playing: " + song_name + "\nBy: " + song_artist)

    @rumps.clicked("Previous Song")
    def prev(self, _):
        sp.previous_track()
    
    @rumps.clicked("Next Song")
    def next(self, _):
        sp.next_track()

    @rumps.clicked("Play/Pause")
    def pp(self, _):
        try:
            sp.start_playback()
        except:
            sp.pause_playback()

if __name__ == '__main__':
    StatusBar().run()