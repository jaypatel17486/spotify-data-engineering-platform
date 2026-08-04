from pathlib import Path
import boto3


BUCKET_NAME = "jaypatel-spotify-data-lake-2026"


def main():

    s3 = boto3.client("s3")

    parquet_file = Path("data/parquet/albums.parquet")

    if not parquet_file.exists():
        raise FileNotFoundError(
            f"{parquet_file} does not exist. Run the ETL pipeline first."
        )

    s3.upload_file(
        str(parquet_file),
        BUCKET_NAME,
        "parquet/albums.parquet",
    )

    print("=" * 60)
    print("✅ Parquet uploaded successfully!")
    print(f"Bucket : {BUCKET_NAME}")
    print("Object : parquet/albums.parquet")
    print("=" * 60)


if __name__ == "__main__":
    main()