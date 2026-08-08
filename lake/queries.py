import duckdb

con = duckdb.connect("spotify.duckdb")

print("=" * 70)
print("Spotify Analytics")
print("=" * 70)

print("\n1. Total Albums")
print(
    con.execute("""
        SELECT COUNT(*) AS total_albums
        FROM albums
    """).fetchdf()
)

print("\n2. Latest Albums")
print(
    con.execute("""
        SELECT
            album_name,
            release_date,
            total_tracks
        FROM albums
        ORDER BY release_date DESC
        LIMIT 10
    """).fetchdf()
)

print("\n3. Average Tracks Per Album")
print(
    con.execute("""
        SELECT
            ROUND(AVG(total_tracks),2) AS avg_tracks
        FROM albums
    """).fetchdf()
)

con.close()