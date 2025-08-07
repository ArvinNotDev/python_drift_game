import os
import json
from .settings_model import Settings

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.json")

# Create settings.json with defaults if it doesn't exist
if not os.path.exists(SETTINGS_FILE):
    os.makedirs(os.path.dirname(SETTINGS_FILE), exist_ok=True)
    default_settings = Settings()
    with open(SETTINGS_FILE, "w") as f:
        f.write(default_settings.model_dump_json(indent=4))
    print("✅ Created default settings.json")

# Load settings from the JSON file
with open(SETTINGS_FILE, "r") as f:
    settings_data = json.load(f)
    settings = Settings(**settings_data)
