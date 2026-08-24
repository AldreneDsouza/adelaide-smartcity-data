import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from google.transit import gtfs_realtime_pb2


API_URL = "https://gtfs.adelaidemetro.com.au/v1/realtime/vehicle_positions"

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


request = urllib.request.Request(
    API_URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)


with urllib.request.urlopen(request, timeout=30) as response:
    raw_data = response.read()


feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(raw_data)


vehicles = []


for entity in feed.entity:

    if not entity.HasField("vehicle"):
        continue

    vehicle = entity.vehicle

    record = {
        "entity_id": entity.id,

        "vehicle_id": (
            vehicle.vehicle.id
            if vehicle.HasField("vehicle") and vehicle.vehicle.HasField("id")
            else None
        ),

        "vehicle_label": (
            vehicle.vehicle.label
            if vehicle.HasField("vehicle") and vehicle.vehicle.HasField("label")
            else None
        ),

        "trip_id": (
            vehicle.trip.trip_id
            if vehicle.HasField("trip") and vehicle.trip.HasField("trip_id")
            else None
        ),

        "route_id": (
            vehicle.trip.route_id
            if vehicle.HasField("trip") and vehicle.trip.HasField("route_id")
            else None
        ),

        "direction_id": (
            vehicle.trip.direction_id
            if vehicle.HasField("trip") and vehicle.trip.HasField("direction_id")
            else None
        ),

        "latitude": (
            vehicle.position.latitude
            if vehicle.HasField("position")
            else None
        ),

        "longitude": (
            vehicle.position.longitude
            if vehicle.HasField("position")
            else None
        ),

        "bearing": (
            vehicle.position.bearing
            if vehicle.HasField("position")
            and vehicle.position.HasField("bearing")
            else None
        ),

        "speed": (
            vehicle.position.speed
            if vehicle.HasField("position")
            else None
        ),

        "stop_id": (
            vehicle.stop_id
            if vehicle.HasField("stop_id")
            else None
        ),

        "timestamp": (
            vehicle.timestamp
            if vehicle.HasField("timestamp")
            else None
        ),
    }

    vehicles.append(record)


output = {
    "ingested_at_utc": timestamp,
    "source": "Adelaide Metro GTFS Realtime Vehicle Positions",
    "vehicle_count": len(vehicles),
    "vehicles": vehicles,
}


# Save timestamped historical snapshot
output_file = OUTPUT_DIR / f"vehicle_positions_{timestamp}.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(output, file, indent=2)


# Save/update the latest snapshot
latest_file = OUTPUT_DIR / "latest_vehicle_positions.json"

with open(latest_file, "w", encoding="utf-8") as file:
    json.dump(output, file, indent=2)


print(f"Saved: {output_file}")
print(f"Updated: {latest_file}")
print(f"Vehicles: {len(vehicles)}")
