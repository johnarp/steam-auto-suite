# For interacting with the computer.
import os

# To copy and paste files.
import shutil

# Typical path for most users.
# Replace [YOUR USER ID] with the folder you see in Steam\userdata\.
# If you installed in a different location, then change the path accordingly.
GRID_PATH = r"C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\grid"

# The folder the script is in, is the same as your artwork.
ASSETS_PATH = os.getcwd()

def main():
    # Gives an error if the GRID_PATH doesn't exist.
    if not os.path.exists(GRID_PATH):
        print(f"Invalid GRID_PATH: {GRID_PATH}")
        return

    # Just telling you where your artwork and where Steam is located.
    print(f"Assets: {ASSETS_PATH}")
    print(f"Steam: {GRID_PATH}\n")

    # Does everything below every time, for every folder.
    for FOLDER in os.listdir(ASSETS_PATH):
        # Creates a new path for a specific game's folder called FOLDER_PATH.
        FOLDER_PATH = os.path.join(ASSETS_PATH, FOLDER)

        # If FOLDER_PATH isn't a folder, ignore it.
        if not os.path.isdir(FOLDER_PATH):
            continue

        # If FOLDER_PATH isn't all numbers, ignore it.
        if not FOLDER.isdigit():
            continue

        # The APP_ID is the name of the folder. 
        APP_ID = FOLDER

        # Does everything below every time, for every artwork.
        for FILE in os.listdir(FOLDER_PATH):
            # Creates a new path for a specific artwork's file called SOURCE.
            SOURCE = os.path.join(FOLDER_PATH, FILE)

            # If SOURCE isn't a file, ignore it.
            if not os.path.isfile(SOURCE):
                continue

            # Creates a new path for where that image will be pasted called DEST.
            DEST = os.path.join(GRID_PATH, FILE)

            # If an image of the same name already exists, it will automatically overwrite it. This is just letting you know.
            if os.path.exists(DEST):
                print(f"[OVERWRITE]: {FILE}")

            # Copies the file from your artwork folder to the Steam folder.
            shutil.copyfile(SOURCE, DEST)
            # Lets you know it all went okay.
            print(f"[OK]: {APP_ID} --> {FILE}")

    # Done.
    print("\nDone.")

# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    main()