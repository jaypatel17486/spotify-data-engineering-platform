-- Total Albums
SELECT COUNT(*) AS total_albums
FROM albums;

-- Albums by Release Year
SELECT
    EXTRACT(YEAR FROM release_date) AS release_year,
    COUNT(*) AS total_albums
FROM albums
GROUP BY release_year
ORDER BY release_year;

-- Average Tracks per Album
SELECT
    ROUND(AVG(total_tracks), 2) AS average_tracks
FROM albums;

-- Album Type Distribution
SELECT
    album_type,
    COUNT(*) AS total
FROM albums
GROUP BY album_type
ORDER BY total DESC;

-- Latest Albums
SELECT
    album_name,
    release_date,
    total_tracks
FROM albums
ORDER BY release_date DESC
LIMIT 10;