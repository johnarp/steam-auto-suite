# To interact with the computer.
import os
# To work with JSON data.
import json
# To work with time.
import time
# To copy and paste files.
import shutil

# Typical path for most users.
# Replace [YOUR USER ID] with the folder you see in Steam\userdata\.
# If you installed in a different location, then change the path accordingly.
CONFIG_PATH = r"C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\cloudstorage\cloud-storage-namespace-1.json"

# The folder the script is in, is the same as your defined favorites.
# Your favorites file must be named "favorites.json".
FAVORITES_FILE = os.path.join(os.getcwd(), "favorites.json")

def main():
    # Gives an error if CONFIG_PATH doesn't exist.
    if not os.path.exists(CONFIG_PATH):
        print(f"Invalid CONFIG_PATH: {CONFIG_PATH}")
        return

    # Gives an error if favorites.json doesn't exist.
    if not os.path.exists(FAVORITES_FILE):
        print(f"favorites.json not found: {FAVORITES_FILE}")
        return

    # Backs up the config file before touching it, just in case.
    BACKUP_PATH = CONFIG_PATH + ".backup"
    shutil.copyfile(CONFIG_PATH, BACKUP_PATH)
    print(f"Backup saved: {BACKUP_PATH}\n")

    # Loads your favorites.json into Python.
    with open(FAVORITES_FILE, "r") as f:
        FAVORITES = json.load(f)

    # Loads Steam's config file. It's a list of [key, object] pairs.
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        DATA = json.load(f)

    # Steam's hardcoded key and ID for the Favorites collection.
    COLLECTION_KEY  = "user-collections.favorite"

    # Builds the inner value object.
    INNER_VALUE = {
        "id": "favorite",
        "name": "Favorites",
        "added": [int(ID) for ID in FAVORITES],
        "removed": []
    }

    # Builds the full entry object.
    NEW_ENTRY = {
        "key": COLLECTION_KEY,
        "timestamp": int(time.time()),
        "value": json.dumps(INNER_VALUE, separators=(",", ":")),
        "conflictResolutionMethod": "custom",
        "strMethodId": "union-collections"
    }

    # Replaces the existing entry if found, or appends a new one.
    REPLACED = False
    for i, ENTRY in enumerate(DATA):
        if ENTRY[0] == COLLECTION_KEY:
            DATA[i] = [COLLECTION_KEY, NEW_ENTRY]
            REPLACED = True
            print("Updated Favorites.")
            break
    if not REPLACED:
        DATA.append([COLLECTION_KEY, NEW_ENTRY])
        print("Created Favorites.")

    # Saves the updated config back to the file.
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(DATA, f, separators=(",", ":"))

    print("Done. Open Steam to see your Favorites.")

# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    main()