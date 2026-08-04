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

    album_files = RAW_PATH.rglob("albums/*.json")

    for file in album_files:

        with open(
            file,
            "r",
            encoding="utf-8",
        ) as f:

            albums = json.load(f)

        for album in albums["items"]:

            album_records.append({

                "album_id": album["id"],

                "album_name": album["name"],

                "album_type": album["album_type"],

                "release_date": album["release_date"],

                "total_tracks": album["total_tracks"],

                "spotify_url": album["external_urls"]["spotify"]

            })

    df = pd.DataFrame(album_records)

    output = PROCESSED_PATH / "albums.csv"

    df.to_csv(
        output,
        index=False,
    )

    print("=" * 60)
    print("Transformation completed")
    print(df.head())
    print("=" * 60)


if __name__ == "__main__":
    main()