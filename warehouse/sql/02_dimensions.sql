CREATE TABLE IF NOT EXISTS warehouse.dim_artist (

    artist_key SERIAL PRIMARY KEY,

    spotify_artist_id VARCHAR(100) UNIQUE,

    artist_name VARCHAR(255),

    spotify_url TEXT
);


CREATE TABLE IF NOT EXISTS warehouse.dim_album (

    album_key SERIAL PRIMARY KEY,

    spotify_album_id VARCHAR(100) UNIQUE,

    artist_key INTEGER
        REFERENCES warehouse.dim_artist(artist_key),

    album_name VARCHAR(255),

    album_type VARCHAR(50),

    release_date DATE,

    total_tracks INTEGER
);


CREATE TABLE IF NOT EXISTS warehouse.dim_track (

    track_key SERIAL PRIMARY KEY,

    spotify_track_id VARCHAR(100) UNIQUE,

    album_key INTEGER
        REFERENCES warehouse.dim_album(album_key),

    track_name VARCHAR(255),

    duration_ms INTEGER,

    explicit BOOLEAN,

    track_number INTEGER
);


CREATE TABLE IF NOT EXISTS warehouse.dim_date (

    date_key SERIAL PRIMARY KEY,

    full_date DATE UNIQUE,

    year INTEGER,

    month INTEGER,

    day INTEGER,

    quarter INTEGER
);