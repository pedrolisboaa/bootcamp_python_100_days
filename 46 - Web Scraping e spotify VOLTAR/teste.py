import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id='b5ba5d19d7754427a1481ce932ef5a3c',
        client_secret='dde775c0d5844f5a9822346f638a8f5b',
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]