from api.spotify_client import SpotifyClient


class SpotifyService:

    def __init__(self):
        self.spotify = SpotifyClient().get_client()

    def search_artist(self, artist_name: str):

        results = self.spotify.search(
            q=artist_name,
            type="artist",
            limit=1,
        )

        return results["artists"]["items"][0]

    def get_artist_albums(self, artist_id: str):

        return self.spotify._get(
            f"artists/{artist_id}/albums"
        )

    def get_album_tracks(self, album_id: str):

        return self.spotify._get(
            f"albums/{album_id}/tracks"
        )