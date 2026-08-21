import json
from datetime import datetime, timezone
from pathlib import Path
import urllib.request

API_URL = "https://gtfs.adelaidemetro.com.au/v1/realtime/vehicle_positions/debug"

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
    data = response.read().decode("utf-8")

output_file = OUTPUT_DIR / f"vehicle_positions_{timestamp}.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(
        {
            "ingested_at_utc": timestamp,
            "source": "Adelaide Metro GTFS Realtime",
            "data": data
        },
        file,
        indent=2
    )

print(f"Saved: {output_file}")
