
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_SECRET = "05a75946f5094398a30e856ad5d5b641"
CLIENT_ID = "aa6187ff73aa4413b47e4a2fe621531b"

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="22bichulre5jpecc2yf6ghfui",
    )
)

date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
user_id = sp.current_user()
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, 'html.parser')
all_songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in all_songs]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create("22bichulre5jpecc2yf6ghfui", (f"{date} Billboard 100"), public=False, collaborative=False, description='Day 45 in 100 days of code')
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
