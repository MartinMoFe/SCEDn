import json
import os

BASE_DIR = r"C:\git\SCED"
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
OBJECTS_DIR = os.path.join(BASE_DIR, "objects")

# ---- Load config.json ----
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

order = config.get("ObjectStates_order", [])

# Normalize names (strip .json if present)
order_set = set(name.replace(".json", "") for name in order)

# ---- Read objects directory ----
objects_set = set()

for entry in os.listdir(OBJECTS_DIR):
    full_path = os.path.join(OBJECTS_DIR, entry)

    if os.path.isdir(full_path):
        objects_set.add(entry)
    elif entry.endswith(".json"):
        objects_set.add(entry.replace(".json", ""))

# ---- Compare ----
missing_in_objects = order_set - objects_set
missing_in_config = objects_set - order_set

# ---- Output ----
print("=== Missing in objects folder ===")
if missing_in_objects:
    for name in sorted(missing_in_objects):
        print(f"  - {name}")
else:
    print("  None")

print("\n=== Missing in ObjectStates_order ===")
if missing_in_config:
    for name in sorted(missing_in_config):
        print(f"  - {name}")
else:
    print("  None")
