from api.extract import main as extract
from etl.transform import main as transform
from etl.parquet import main as parquet
from lake.s3_upload import main as upload
from etl.load import main as load


def main():

    print("=" * 60)
    print("Spotify Data Engineering Pipeline Started")
    print("=" * 60)

    extract()

    transform()

    parquet()

    upload()

    load()

    print("=" * 60)
    print("Spotify Data Engineering Pipeline Completed")
    print("=" * 60)


if __name__ == "__main__":
    main()