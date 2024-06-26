
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_SECRET = "05a75946f5094398a30e856ad5d5b641"
CLIENT_ID = "aa6187ff73aa4413b47e4a2fe621531b"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="22bichulre5jpecc2yf6ghfui",
    )
)

genre = input("Which genre do you want a playlist for? ")
genre_no_space = genre.replace(' ', '')
user_id = sp.current_user()

response = requests.get(f"https://everynoise.com/engenremap-{genre_no_space}.html")
website = response.text

# getting song names and artists
songs_final = []
soup = BeautifulSoup(website, 'html.parser')
all_songs = soup.find_all("div", class_="genre scanme")
for song in all_songs:
    songs = (song["title"])
    songs_final.append(songs.replace('e.g. ', '', 1))

# song links
song_uris = []
for song in songs_final:
    result = sp.search(q=f"track:{song}", type="track", market="LT")
    if result["tracks"]["items"]:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        if len(song_uris) == 100:
            break
    else:
        print(f"{song} wasn't found :(")

# adding to playlist
playlist = sp.user_playlist_create("22bichulre5jpecc2yf6ghfui", (f"{genre}"), public=False,
                                       collaborative=False, description='From EveryNoiseAtOnce.com :)')
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
