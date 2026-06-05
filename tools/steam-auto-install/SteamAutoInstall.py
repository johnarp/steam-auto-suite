# To interact with the computer.
import os
# To work with JSON data.
import json
# To run system commands.
import subprocess
# To wait between installs.
import time

# The folder the script is in, is the same as your defined installs.
# Your installs file must be named "install.json".
INSTALL_FILE = os.path.join(os.getcwd(), "install.json")

# Seconds to wait between each uninstall dialog.
# Increase this if Steam isn't keeping up.
DELAY = 5

def main():
    # Gives an error if install.json doesn't exist.
    if not os.path.exists(INSTALL_FILE):
        print(f"install.json not found: {INSTALL_FILE}")
        return

    # Loads your install.json into Python.
    with open(INSTALL_FILE, "r") as f:
        APP_IDS = json.load(f)

    # For each App ID, open the Steam install dialog.
    for APP_ID in APP_IDS:
        print(f"[INSTALLING]: {APP_ID}")
        subprocess.run(["start", f"steam://install/{APP_ID}"], shell=True)
        time.sleep(DELAY)

    print("\nDone.")


# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    main()