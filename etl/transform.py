import json
from pathlib import Path

import pandas as pd

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")


def main():

    PROCESSED_PATH.mkdir(
        parents=True,
        exist_ok=True,
    )

    album_records = []
    artist_records = []

    album_files = RAW_PATH.rglob("albums/*.json")

    for file in album_files:

        with open(
            file,
            "r",
            encoding="utf-8",
        ) as f:

            albums = json.load(f)

        for album in albums["items"]:

            # First artist on the album
            artist = album["artists"][0]

            artist_records.append(
                {
                    "artist_id": artist["id"],
                    "artist_name": artist["name"],
                    "spotify_url": artist["external_urls"]["spotify"],
                }
            )

            album_records.append(
                {
                    "album_id": album["id"],
                    "artist_id": artist["id"],
                    "album_name": album["name"],
                    "album_type": album["album_type"],
                    "release_date": album["release_date"],
                    "total_tracks": album["total_tracks"],
                    "spotify_url": album["external_urls"]["spotify"],
                }
            )

    albums_df = pd.DataFrame(album_records)

    artists_df = (
        pd.DataFrame(artist_records)
        .drop_duplicates(subset=["artist_id"])
        .reset_index(drop=True)
    )

    albums_df.to_csv(
        PROCESSED_PATH / "albums.csv",
        index=False,
    )

    artists_df.to_csv(
        PROCESSED_PATH / "artists.csv",
        index=False,
    )

    print("=" * 60)
    print("Transformation completed")
    print("=" * 60)

    print("\nAlbums")
    print(albums_df.head())

    print("\nArtists")
    print(artists_df.head())

    print("\nFiles Created")
    print("- albums.csv")
    print("- artists.csv")

    print("=" * 60)


if __name__ == "__main__":
    main()