import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=st.secrets["spotify"]["client_id"],
        client_secret=st.secrets["spotify"]["client_secret"]
    ))

def get_recommendations(genre):
    sp = get_spotify_client()
    recs = sp.recommendations(seed_genres=[genre], limit=5)
    return [{
        "name": t["name"],
        "artist": t["artists"][0]["name"],
        "url": t["external_urls"]["spotify"],
        "img": t["album"]["images"][0]["url"]
    } for t in recs["tracks"]]

