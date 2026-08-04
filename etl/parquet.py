from pathlib import Path

import pandas as pd


def main():

    processed = Path("data/processed/albums.csv")

    parquet_dir = Path("data/parquet")

    parquet_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    df = pd.read_csv(processed)

    output = parquet_dir / "albums.parquet"

    df.to_parquet(
        output,
        index=False,
    )

    print("=" * 60)
    print("Parquet created successfully")
    print(output)
    print("=" * 60)


if __name__ == "__main__":
    main()