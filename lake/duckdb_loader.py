from pathlib import Path
import duckdb


def main():

    parquet_file = Path("data/parquet/albums.parquet")

    con = duckdb.connect("spotify.duckdb")

    con.execute(
        """
        CREATE OR REPLACE TABLE albums AS
        SELECT *
        FROM read_parquet(?)
        """,
        [str(parquet_file)],
    )

    print("=" * 60)
    print("DuckDB database created successfully.")
    print("=" * 60)

    con.close()


if __name__ == "__main__":
    main()