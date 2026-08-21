CREATE OR REPLACE TABLE vehicle_positions_clean AS

SELECT
    ingested_at_utc,
    source,
    entity_id,
    vehicle_id,
    vehicle_label,
    trip_id,
    route_id,
    direction_id,
    latitude,
    longitude,
    bearing,
    speed,
    stop_id,
    timestamp AS vehicle_timestamp_unix,
    to_timestamp(from_unixtime(timestamp)) AS vehicle_timestamp_utc

FROM vehicle_positions

WHERE latitude IS NOT NULL
  AND longitude IS NOT NULL;
