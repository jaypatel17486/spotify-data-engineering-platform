CREATE INDEX idx_artist
ON warehouse.dim_artist(spotify_artist_id);

CREATE INDEX idx_album
ON warehouse.dim_album(spotify_album_id);

CREATE INDEX idx_track
ON warehouse.dim_track(spotify_track_id);