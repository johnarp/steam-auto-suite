# Install the required library through a terminal:
# pip install requests

# To read command-line arguments.
import sys

# To make web requests.
import requests

def main(APP_ID):
    # Steam's app details endpoint link.
    STORE = "https://store.steampowered.com/api/appdetails/"

    # Parameters for the search. appids is the ID, cc is region, and l is language.
    PARAMS = {"appids": APP_ID, "cc": "us", "l": "en"}

    # Send the request and parse the JSON response into a Python dict.
    DATA = requests.get(STORE, params=PARAMS).json()

    # Results from Steam.
    APP_DATA = DATA.get(str(APP_ID), {})

    # If request failed or app doesn't exist.
    if not APP_DATA.get("success"):
        return f"Not Found: {APP_ID}"

    # Extract the data.
    DETAILS = APP_DATA.get("data", {})

    # Get the name.
    NAME = DETAILS.get("name")

    # If there's no name.
    if not NAME:
        return f"Name not found for ID: {APP_ID}"

    # Returns the App ID and the game's name.
    return f"{APP_ID} - {NAME}"

# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    # If the user didn't type any names, show them how to use the script.
    if len(sys.argv) < 2:
        print('Proper Usage: python SteamAutoName.py "app ID"')
        sys.exit(1)

    # For everything typed after 'python SteamAppName.py', do the script
    for ID in sys.argv[1:]:
        print(main(ID))