import json
from pathlib import Path

import pandas as pd

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")


def main():

    track_records = []

    track_files = RAW_PATH.rglob("tracks/*.json")

    for file in track_files:

        album_id = file.stem

        with open(
            file,
            "r",
            encoding="utf-8",
        ) as f:

            tracks = json.load(f)

        for track in tracks["items"]:

            artist = track["artists"][0]

            track_records.append(
                {
                    "track_id": track["id"],
                    "album_id": album_id,
                    "artist_id": artist["id"],
                    "artist_name": artist["name"],
                    "track_name": track["name"],
                    "duration_ms": track["duration_ms"],
                    "track_number": track["track_number"],
                    "explicit": track["explicit"],
                    "spotify_url": track["external_urls"]["spotify"],
                }
            )

    df = pd.DataFrame(track_records)

    df.to_csv(
        PROCESSED_PATH / "tracks.csv",
        index=False,
    )

    print("=" * 60)
    print("Tracks Transformation Completed")
    print("=" * 60)

    print(df.head())

    print("\nTotal Tracks:", len(df))


if __name__ == "__main__":
    main()