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

    df = pd.read_csv(
        "data/processed/albums.csv"
    )

    df.to_sql(
        name="albums",
        con=engine,
        if_exists="replace",
        index=False,
    )

    print("=" * 60)
    print("Albums loaded successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()