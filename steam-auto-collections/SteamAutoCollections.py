# To interact with the computer.
import os
# To work with JSON data.
import json
# To work with time.
import time
# To perform random operations.
import random
# To manipulate strings.
import string
# To copy and paste files.
import shutil

# Typical path for most users.
# Replace [YOUR USER ID] with the folder you see in Steam\userdata\.
# If you installed in a different location, then change the path accordingly.
CONFIG_PATH = r"C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\cloudstorage\cloud-storage-namespace-1.json"

# The folder the script is in, is the same as your defined collections.
# Your collections file must be named "collections.json".
COLLECTIONS_FILE = os.path.join(os.getcwd(), "collections.json")


def generate_id():
    # Generates a random 14-character ID to match Steam's format.
    CHARS = string.ascii_letters + string.digits
    return "uc-" + "".join(random.choices(CHARS, k=14))


def main():
    # Gives an error if CONFIG_PATH doesn't exist.
    if not os.path.exists(CONFIG_PATH):
        print(f"Invalid CONFIG_PATH: {CONFIG_PATH}")
        return

    # Gives an error if collections.json doesn't exist.
    if not os.path.exists(COLLECTIONS_FILE):
        print(f"collections.json not found: {COLLECTIONS_FILE}")
        return

    # Backs up the config file before touching it, just in case.
    BACKUP_PATH = CONFIG_PATH + ".backup"
    shutil.copyfile(CONFIG_PATH, BACKUP_PATH)
    print(f"Backup saved: {BACKUP_PATH}\n")

    # Loads your collections.json into Python.
    with open(COLLECTIONS_FILE, "r") as f:
        COLLECTIONS = json.load(f)

    # Loads Steam's config file. It's a list of [key, object] pairs.
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        DATA = json.load(f)

    # For each collection you defined, create or update it.
    for NAME, APP_IDS in COLLECTIONS.items():
        COLLECTION_KEY = None

        # Checks if a collection with this name already exists.
        for ENTRY in DATA:
            KEY, OBJ = ENTRY

            # Skip deleted entries and non-collection entries.
            if not KEY.startswith("user-collections."):
                continue
            if OBJ.get("is_deleted"):
                continue
            if "value" not in OBJ:
                continue

            # Parse the inner value to check the name.
            INNER = json.loads(OBJ["value"])
            if INNER.get("name") == NAME:
                COLLECTION_KEY = KEY
                print(f"[UPDATE]: {NAME}")
                break

        # If it doesn't exist, generate a new key for it.
        if COLLECTION_KEY is None:
            COLLECTION_KEY = "user-collections." + generate_id()
            print(f"[CREATE]: {NAME}")

        # Build the inner value object. App IDs must be integers.
        INNER_VALUE = {
            "id":      COLLECTION_KEY.replace("user-collections.", ""),
            "name":    NAME,
            "added":   [int(ID) for ID in APP_IDS],
            "removed": []
        }

        # Build the full entry object.
        NEW_ENTRY = {
            "key":                      COLLECTION_KEY,
            "timestamp":                int(time.time()),
            "value":                    json.dumps(INNER_VALUE, separators=(",", ":")),
            "conflictResolutionMethod": "custom",
            "strMethodId":              "union-collections"
        }

        # Replace the existing entry if found, or append a new one.
        REPLACED = False
        for i, ENTRY in enumerate(DATA):
            if ENTRY[0] == COLLECTION_KEY:
                DATA[i] = [COLLECTION_KEY, NEW_ENTRY]
                REPLACED = True
                break
        if not REPLACED:
            DATA.append([COLLECTION_KEY, NEW_ENTRY])

    # Saves the updated config back to the file.
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(DATA, f, separators=(",", ":"))

    print("\nDone. Open Steam to see your collections.")


# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    main()