import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from spotipy.exceptions import SpotifyException

answer=input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD:")
website_base = "https://appbrewery.github.io/bakeboard-hot-100/"
request = requests.get(website_base + answer)
status = request.status_code
match status:
    case 200:
        print("Data found! Let's see...")
    case 404:
        print("This date is not recorded :(")
        exit()
    case _:
        print(f"Unexpected status code: {status}")
        exit()
soup = BeautifulSoup(request.content, "html.parser")
songs = soup.find_all(name="h3", class_="chart-entry__title")
song_titles = [song.get_text().strip() for song in songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="...",
    client_secret="...",
    redirect_uri="...",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]

song_uris = []
for title in song_titles:
    while True:
        try:
            result = sp.search(q=f"track:{title}", type="track")
            break
        except SpotifyException as e:
            if e.http_status == 429:
                retry_after = int(e.headers.get("Retry-After", 1))
                print(f"Rate limited, waiting {retry_after}s...")
                time.sleep(retry_after)
            else:
                raise
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} not found on Spotify, skipping...")
    time.sleep(0.1)

try:
    playlist = sp.playlist_create_for_current_user(
        name=f"{answer} Billboard Hot 100",
        public=False
    )
except AttributeError:
    token = sp.auth_manager.get_access_token(as_dict=False)
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.post(
        "https://api.spotify.com/v1/me/playlists",
        headers=headers,
        json={"name":f"{answer} Billboard Hot 100" , "public": False}
    )
    response.raise_for_status()
    playlist = response.json()

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("Playlist created!")
print("Open it here:", playlist["external_urls"]["spotify"])