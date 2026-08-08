from config.settings import ARTISTS

from api.spotify_service import SpotifyService
from api.save_json import save_json


def main():

    spotify = SpotifyService()

    for artist_name in ARTISTS:

        print(f"\nExtracting {artist_name}...")

        artist = spotify.search_artist(artist_name)

        save_json(
            artist,
            "artists",
            f"{artist_name.replace(' ', '_').lower()}.json",
        )

        albums = spotify.get_artist_albums(
            artist["id"]
        )

        save_json(
            albums,
            "albums",
            f"{artist_name.replace(' ', '_').lower()}.json",
        )

        # NEW: Download tracks for every album
        for album in albums["items"]:

            print(f"   Downloading tracks for {album['name']}")

            tracks = spotify.get_album_tracks(
                album["id"]
            )

            save_json(
                tracks,
                "tracks",
                f"{album['id']}.json",
            )

    print("\n✅ Extraction completed successfully.")


if __name__ == "__main__":
    main()