import pandas as pd
from pandas import json_normalize

import requests 
import json
import os
from dotenv import load_dotenv #conda install -c conda-forge python-dotenv

import time

import sys
sys.path.append("../")

from getpass import getpass


# get token
def get_token():
    url_token = "https://accounts.spotify.com/api/token"
    CLIENT_SECRET = getpass()
    CLIENT_ID = "d590634c7439463cba572d482c9f0882"
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    response = requests.post('https://accounts.spotify.com/api/token', data=data)
    return response.json()['access_token']



# request playlist function
def spotify_request_playlist(endpoint,token):
    url = "https://api.spotify.com/v1/playlists/"
    headers = {'Authorization': f'Bearer {token}'}
    try:
        res = requests.get(url+endpoint, headers=headers)
        return res.json()
    except:
        return 'too many requests'
    


# request feature track function
def spotify_request_features(endpoint,token):
    url = "https://api.spotify.com/v1/audio-features/"
    headers = {'Authorization': f'Bearer {token}'}
    try:
        res = requests.get(url+endpoint, headers=headers)
        return res.json()
    except:
        return 'too many requests'
    



#extraxtion through Spotify API
def playlists(dict_):
    list_tracks_dict = []
    token = get_token()
    for k,v in dict_:
        playlist_data = spotify_request_playlist(v,token)
        tracks = playlist_data['tracks']['items']
        time.sleep(1)
        for track in tracks:
            track_dict = {}
            track_dict["track_id"] = track['track']['id']
            track_dict["track_name"] = track['track']['name']
            track_dict["track_artist"] = ', '.join([artist['name'] for artist in track['track']['album']['artists']])
            track_dict["track_popularity"] = track['track']['popularity']
            track_dict["track_album_release_date"] = track['track']['album']['release_date']
            track_dict["playlist_name"] = k 
            track_dict["playlist_id"] = v
            list_tracks_dict=list_tracks_dict+[track_dict]
    return list_tracks_dict

def features(list_of_dict):
    token = get_token()
    for el in list_of_dict:
        endpoint_track = el["track_id"]
        track_data = spotify_request_features(endpoint_track,token)
        time.sleep(2)
        el["danceability"] = track_data['danceability']
        el["energy"] = track_data["energy"]
        el["valence"] = track_data["valence"]
    return list_of_dict

def dataframe_from_api(dict_playlists, path):
    list_tracks = playlists(dict_playlists)
    list_tracks = features(list_tracks)
    songs_df = pd.DataFrame(list_tracks)
    songs_df.to_csv("path")
    return songs_df