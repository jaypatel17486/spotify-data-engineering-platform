CREATE TABLE IF NOT EXISTS warehouse.fact_track_metrics (

    fact_key SERIAL PRIMARY KEY,

    artist_key INTEGER
        REFERENCES warehouse.dim_artist(artist_key),

    album_key INTEGER
        REFERENCES warehouse.dim_album(album_key),

    track_key INTEGER
        REFERENCES warehouse.dim_track(track_key),

    date_key INTEGER
        REFERENCES warehouse.dim_date(date_key),

    popularity INTEGER
);