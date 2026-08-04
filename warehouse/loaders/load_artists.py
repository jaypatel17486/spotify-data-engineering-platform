import json
from pathlib import Path

from warehouse.loaders.database import get_connection
from warehouse.loaders.base_loader import BaseLoader

loader = BaseLoader()

loader.execute(...)

loader.commit()

loader.close()

RAW_PATH = Path("data/raw")


def main():

    conn = get_connection()
    cur = conn.cursor()

    artist_files = RAW_PATH.rglob("artists/*.json")

    for file in artist_files:

        with open(file, "r", encoding="utf-8") as f:
            artist = json.load(f)

        cur.execute(
            """
            INSERT INTO warehouse.dim_artist
            (
                spotify_artist_id,
                artist_name,
                spotify_url
            )

            VALUES (%s,%s,%s)

            ON CONFLICT (spotify_artist_id)
            DO NOTHING
            """,
            (
                artist["id"],
                artist["name"],
                artist["external_urls"]["spotify"],
            ),
        )

    conn.commit()

    cur.close()
    conn.close()

    print("Artists Loaded Successfully")


if __name__ == "__main__":
    main()