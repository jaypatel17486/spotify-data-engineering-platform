CREATE OR REPLACE VIEW warehouse.v_track_summary AS

SELECT

    a.artist_name,

    al.album_name,

    t.track_name,

    t.duration_ms,

    f.popularity

FROM warehouse.fact_track_metrics f

JOIN warehouse.dim_artist a
ON f.artist_key = a.artist_key

JOIN warehouse.dim_album al
ON f.album_key = al.album_key

JOIN warehouse.dim_track t
ON f.track_key = t.track_key;