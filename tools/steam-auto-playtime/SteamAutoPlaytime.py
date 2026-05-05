# To interact with the computer.
import os
# To work with JSON data.
import json
# To copy and paste files.
import shutil

# Typical path for most users.
# Replace [YOUR USER ID] with the folder you see in Steam\userdata\.
# If you installed in a different location, then change the path accordingly.
CONFIG_PATH = r"C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\localconfig.vdf"

# The folder the script is in, is the same as your defined playtime.
# Your playtime file must be named "playtime.json".
PLAYTIME_FILE = os.path.join(os.getcwd(), "playtime.json")


def set_playtime(LINES, APP_ID, MINUTES):
    # Scans through the file line by line looking for the app ID block.
    i = 0
    while i < len(LINES):

        # If this line is exactly the app ID as a quoted key, we found it.
        if LINES[i].strip() == f'"{APP_ID}"':

            # Note the indentation so we can match it later.
            INDENT = LINES[i][:len(LINES[i]) - len(LINES[i].lstrip())]

            # Find the opening brace that follows.
            j = i + 1
            while j < len(LINES) and LINES[j].strip() == '':
                j += 1

            # If the next non-empty line is {, we're inside the right block.
            if j < len(LINES) and LINES[j].strip() == '{':

                # Find the matching closing brace by tracking depth.
                DEPTH = 1
                k = j + 1
                while k < len(LINES) and DEPTH > 0:
                    S = LINES[k].strip()
                    if S == '{':
                        DEPTH += 1
                    elif S == '}':
                        DEPTH -= 1
                    k += 1

                # k - 1 is now the index of the matching closing brace.
                CLOSE = k - 1

                # Search within the block for an existing Playtime entry.
                INNER_INDENT = INDENT + '\t'
                FOUND = False
                for m in range(j + 1, CLOSE):
                    if LINES[m].strip().startswith('"Playtime"'):
                        # Replace it with the new value.
                        LINES[m] = f'{INNER_INDENT}"Playtime"\t\t"{MINUTES}"\n'
                        FOUND = True
                        break

                # If there was no existing Playtime, insert one before the closing brace.
                if not FOUND:
                    LINES.insert(CLOSE, f'{INNER_INDENT}"Playtime"\t\t"{MINUTES}"\n')

                return True

        i += 1

    # App ID wasn't found anywhere in the file.
    return False


def main():
    # Gives an error if CONFIG_PATH doesn't exist.
    if not os.path.exists(CONFIG_PATH):
        print(f"Invalid CONFIG_PATH: {CONFIG_PATH}")
        return

    # Gives an error if playtime.json doesn't exist.
    if not os.path.exists(PLAYTIME_FILE):
        print(f"playtime.json not found: {PLAYTIME_FILE}")
        return

    # Backs up the config file before touching it, just in case.
    BACKUP_PATH = CONFIG_PATH + ".backup"
    shutil.copyfile(CONFIG_PATH, BACKUP_PATH)
    print(f"Backup saved: {BACKUP_PATH}\n")

    # Loads your playtime.json into Python.
    with open(PLAYTIME_FILE, "r") as f:
        PLAYTIME = json.load(f)

    # Loads Steam's localconfig.vdf as a list of lines.
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        LINES = f.readlines()

    # For each app ID and its playtime, try to apply it.
    for APP_ID, MINUTES in PLAYTIME.items():
        SUCCESS = set_playtime(LINES, str(APP_ID), int(MINUTES))
        if SUCCESS:
            print(f"[OK]: {APP_ID} --> {MINUTES}m")
        else:
            # This usually means the game has never been launched or doesn't exist in the config yet.
            print(f"[NOT FOUND]: {APP_ID}")

    # Saves the updated config back to the file.
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.writelines(LINES)

    print("\nDone. Open Steam to see your playtime.")


# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    main()