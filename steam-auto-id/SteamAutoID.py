# Install the required library through a terminal:
# pip install requests

# To read command-line arguments.
import sys

# To make web requests.
import requests

def main(QUERY):
    # Steam's store search endpoint link.
    STORE = "https://store.steampowered.com/api/storesearch/"

    # Parameters for the search. Term is the game name, cc is region, and l is language.
    PARAMS = {"term": QUERY, "cc": "us", "l": "en"}

    # Send the request and parse the JSON response into a Python dict.
    DATA = requests.get(STORE, params=PARAMS).json()

    # The list of search result that Steam sends back.
    ITEMS = DATA.get("items", [])

    # If Steam found nothing, let you know.
    if not ITEMS:
        return f"Not Found: {QUERY}"

    # Take the top result, the most relevant match.
    TOP = ITEMS[0]

    # Return the App ID and the game's name.
    return f"{TOP['id']} - {TOP['name']}"

# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    # If the user didn't type any names, show them how to use the script.
    if len(sys.argv) < 2:
        print('Proper Usage: python SteamAutoID.py "game name"')
        sys.exit(1)

    # For everything typed after 'python SteamAppID.py', do the script
    for GAME in sys.argv[1:]:
        print(main(GAME))