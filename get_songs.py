import spotipy
from spotipy.oauth2 import SpotifyOAuth

def write_songs(client_id, client_secret, redirect_uri):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read'))
    results = sp.current_user_saved_tracks()
    song_list = []
    for item in results['items']:
        track = item['track']
        song_list.append(track['name'] + ', ' + ', '.join([artist['name'] for artist in track['artists']]))
    songs = "\n".join(song_list)
    with open('./text_files/songs_list.txt', 'w') as file:
        file.write(songs)
