# To interact with the computer.
import os
# To work with JSON data.
import json
# To run system commands.
import subprocess
# To wait between installs.
import time

# The folder the script is in, is the same as your defined uninstalls.
# Your uninstalls file must be named "uninstall.json".
UNINSTALL_FILE = os.path.join(os.getcwd(), "uninstall.json")

# Seconds to wait between each uninstall dialog.
# Increase this if Steam isn't keeping up.
DELAY = 5

def main():
    # Gives an error if uninstall.json doesn't exist.
    if not os.path.exists(UNINSTALL_FILE):
        print(f"uninstall.json not found: {UNINSTALL_FILE}")
        return

    # Loads your uninstall.json into Python.
    with open(UNINSTALL_FILE, "r") as f:
        APP_IDS = json.load(f)

    # For each App ID, open the Steam uninstall dialog.
    for APP_ID in APP_IDS:
        print(f"[UNINSTALLING]: {APP_ID}")
        subprocess.run(["start", f"steam://uninstall/{APP_ID}"], shell=True)
        time.sleep(DELAY)

    print("\nDone.")


# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    main()