import json
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)


def load_data():
    data_dir = "./data"

    try:
        # Find all files matching the pattern
        files = [f for f in os.listdir(data_dir) if f.startswith("YT_data_") and f.endswith(".json")]
        
        if not files:
            raise FileNotFoundError("No YT_data_*.json files found in ./data directory")

        # Sort by date part in filename
        files.sort(key=lambda x: datetime.strptime(x.replace("YT_data_", "").replace(".json", ""), "%Y-%m-%d"))

        latest_file = files[-1]  # newest one
        file_path = os.path.join(data_dir, latest_file)

        logger.info(f"Processing latest file: {latest_file}")

        with open(file_path, "r", encoding="utf-8") as raw_data:
            data = json.load(raw_data)
        return data

    except FileNotFoundError as e:
        logger.error(str(e))
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
        raise
