CREATE OR REPLACE TABLE vehicle_positions AS

SELECT
    ingested_at_utc,
    source,
    vehicle.entity_id,
    vehicle.vehicle_id,
    vehicle.vehicle_label,
    vehicle.trip_id,
    vehicle.route_id,
    vehicle.direction_id,
    vehicle.latitude,
    vehicle.longitude,
    vehicle.bearing,
    vehicle.speed,
    vehicle.stop_id,
    vehicle.timestamp

FROM json.`abfss://Adelaider_SmartCity_Operations@onelake.dfs.fabric.microsoft.com/Adelaide_SmartCity_Lakehouse.Lakehouse/Files/raw/data_524aaf32-29ee-4ff5-85c5-2c8bb8088486_16442a57-bb22-407a-ae46-3136bbd0db82.json`

LATERAL VIEW explode(vehicles) exploded AS vehicle;
