import duckdb

con = duckdb.connect()

result = con.execute("""
SELECT
    album_name,
    release_date,
    total_tracks
FROM read_parquet('data/parquet/albums.parquet')
ORDER BY release_date DESC
LIMIT 10
""").fetchdf()

print(result)

con.close()