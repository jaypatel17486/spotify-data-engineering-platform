import pandas as pd
from sqlalchemy import create_engine

from config.database import DB_CONFIG


def main():

    DATABASE_URL = (
        f"postgresql://"
        f"{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}"
        f"/{DB_CONFIG['database']}"
    )

    engine = create_engine(DATABASE_URL)

    tables = {
        "artists": "data/processed/artists.csv",
        "albums": "data/processed/albums.csv",
        "tracks": "data/processed/tracks.csv",
    }

    for table_name, csv_path in tables.items():

        print(f"\nLoading {table_name}...")

        df = pd.read_csv(csv_path)

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False,
        )

        print(f"✓ {table_name} loaded ({len(df)} rows)")

    print("\n" + "=" * 60)
    print("All tables loaded successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()