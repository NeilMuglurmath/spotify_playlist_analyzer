import secrets
from spotipy.oauth2 import SpotifyClientCredentials
import os
import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

from secrets import *

# get username from terminal
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# Setting OAuth
auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI,
                            scope=scope)

# create Spotify object
sp = spotipy.Spotify(auth_manager=auth_manager)

currPlaylists = sp.current_user_playlists()
saucePlaylist = currPlaylists['items'][0]['id']
saucePlaylist = sp.playlist(saucePlaylist)['tracks']['items']

features = []
d = {}

for song in saucePlaylist:
    d[song['track']['id']] = song['track']['name']
    features.append(sp.audio_features(song['track']['id']))


while True:
    print('>>>a: acousticness, d: danceability, du: duration, e: energy, k: key, l: liveness, lo: loudness, t: tempo, q: quit')
    feature = input(
        f">>>What feature do you want to Analyze, {sp.current_user()['display_name']}? ")

    if feature == 'a':
        features = sorted(
            features, key=lambda x: x[0]['acousticness'], reverse=True)
        for f in features:
            trackName = d[f[0]['id']]
            acousticness = f[0]['acousticness']
            print(f"Track name: {trackName}, Acousticness: {acousticness}")

    elif feature == 'd':
        features = sorted(
            features, key=lambda x: x[0]['danceability'], reverse=True)
        for f in features:
            trackName = d[f[0]['id']]
            danceability = f[0]['danceability']
            print(f"Track name: {trackName}, danceability: {danceability}")

    elif feature == 'du':
        features = sorted(
            features, key=lambda x: x[0]['duration_ms'], reverse=True)
        for f in features:
            trackName = d[f[0]['id']]
            duration = f[0]['duration_ms']
            print(f"Track name: {trackName}, duration: {duration}")

    elif feature == 'e':
        features = sorted(
            features, key=lambda x: x[0]['energy'], reverse=True)
        for f in features:
            trackName = d[f[0]['id']]
            energy = f[0]['energy']
            print(f"Track name: {trackName}, energy: {energy}")

    elif feature == 'k':
        features = sorted(
            features, key=lambda x: x[0]['key'], reverse=True)
        for f in features:
            trackName = d[f[0]['id']]
            key = f[0]['key']
            print(f"Track name: {trackName}, key: {key}")

    elif feature == 'l':
        features = sorted(
            features, key=lambda x: x[0]['liveness'], reverse=True)
        for f in features:
            trackName = d[f[0]['id']]
            liveness = f[0]['liveness']
            print(f"Track name: {trackName}, liveness: {liveness}")

    elif feature == 'lo':
        features = sorted(
            features, key=lambda x: x[0]['loudness'], reverse=True)
        for f in features:
            trackName = d[f[0]['id']]
            loudness = f[0]['loudness']
            print(f"Track name: {trackName}, loudness: {loudness}")

    elif feature == 't':
        features = sorted(
            features, key=lambda x: x[0]['tempo'], reverse=True)
        for f in features:
            trackName = d[f[0]['id']]
            tempo = f[0]['tempo']
            print(f"Track name: {trackName}, tempo: {tempo}")
    elif feature == 'q':
        break
# print(json.dumps(VARIABLE, sort_keys=True,indent=4))
