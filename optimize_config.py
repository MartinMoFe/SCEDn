import json
import os
import shutil

# Paths
CONFIG_PATH = r"C:\git\SCED\config.json"
OBJECTS_DIR = r"C:\git\SCED\objects"

# Updated list with both spaced and condensed versions
PREFIXES_TO_REMOVE = [
    "Decoration-Coin",
    "CampaignImporterExporter",
    "RulesReference",
    "Doomtokens",
    "Cluetokens",
    "DeckInstructionGenerator",
    "LatestFAQ",
    "SCEDTour",
    "LeadInvestigator",
    "CardBack Enhancer",
    "Connectionmarkers",
    "CardBackEnhancer",
    "WhentheWorldScreamed",
    "FilmFatale",
    "Core2026BrethrenofAsh",
    "Decoration-Ammo"
    "Chapter1-Documents",
    "TableLeg",
    "DetailedPhaseReference",
    "TarotDeck",
    "ScriptedTarotDeckBag",
    "ExpansionGuide",
    "DeckInstructionGenerator",
    "ContentIndicator",
    "TheDrownedCity",
    "CoreNightoftheZealot.64a613"
]

def clean_sced_files():
    if not os.path.exists(CONFIG_PATH):
        print(f"Error: {CONFIG_PATH} not found.")
        return

    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    original_list = data.get("ObjectStates_order", [])
    updated_list = []
    removed_items = []

    # Prepare prefixes for a case-insensitive check
    search_prefixes = [p.lower() for p in PREFIXES_TO_REMOVE]

    for item in original_list:
        item_lower = item.lower()
        # Check if the item starts with any of our defined prefixes (case-insensitive)
        should_remove = any(item_lower.startswith(p) for p in search_prefixes)
        
        if should_remove:
            removed_items.append(item)
        else:
            updated_list.append(item)

    # Save the updated JSON
    data["ObjectStates_order"] = updated_list
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"Updated config.json. Removed {len(removed_items)} entries.")

    # File System Cleanup
    for item in removed_items:
        json_file = os.path.join(OBJECTS_DIR, f"{item}.json")
        folder_path = os.path.join(OBJECTS_DIR, item)

        if os.path.exists(json_file):
            try:
                os.remove(json_file)
                print(f"Deleted file: {item}.json")
            except Exception as e:
                print(f"Error deleting file {item}.json: {e}")

        if os.path.isdir(folder_path):
            try:
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {item}")
            except Exception as e:
                print(f"Error deleting folder {item}: {e}")

if __name__ == "__main__":
    clean_sced_files()
    print("--- Cleanup complete ---")