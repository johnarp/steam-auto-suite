# Install the required library through a terminal:
# pip install requests

# To read command-line arguments.
import sys

# To make web requests.
import requests

def search(QUERY, COUNT):
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
        return [f"Not Found: {QUERY}"]

    # Clamp COUNT to however many results Steam actually returned.
    COUNT = min(COUNT, len(ITEMS))

    # Build a list of results, one line per result.
    RESULTS = []
    for i in range(COUNT):
        RESULTS.append(f"{ITEMS[i]['id']} - {ITEMS[i]['name']}")

    return RESULTS

def parse_args(ARGS):
    # Parses sys.argv into a list of (query, count) pairs and whether --all was passed.
    # Example: "battlefield" -5 "silksong" --all
    # Result: [("battlefield", 5), ("silksong", 1)], all_flag=True

    # Check if --all was passed anywhere in the arguments.
    ALL_FLAG = "--all" in ARGS

    # Remove -all from the list so it doesn't interfere with parsing.
    ARGS = [A for A in ARGS if A != "--all"]

    # Each entry is a (query, count) pair. Count defaults to 1.
    QUERIES = []

    i = 0
    while i < len(ARGS):
        ARG = ARGS[i]

        # If this argument looks like -N (a dash followed by digits), it's a count modifier.
        if ARG.startswith("-") and ARG[1:].isdigit():
            # Applies to the query directly to the left, if one exists.
            if QUERIES:
                QUERY, _ = QUERIES[-1]
                QUERIES[-1] = (QUERY, int(ARG[1:]))
        else:
            # Otherwise, it's a game name. Add it with a default count of 1.
            QUERIES.append((ARG, 1))
        i += 1

    return QUERIES, ALL_FLAG

# Makes sure this file only runs if it's executed directly. No biggie.
if __name__ == "__main__":
    # If the user didn't type any names, show them how to use the script.
    if len(sys.argv) < 2:
        print('Proper Usage: python SteamAutoID.py "game name"')
        print('              python SteamAutoID.py "game name" -3')
        print('              python SteamAutoID.py "game one" -3 "game two"')
        print('              python SteamAutoID.py "game one" "game two" -3 --all')
        sys.exit(1)

    # Parse the arguments into queries and an --all flag.
    QUERIES, ALL_FLAG = parse_args(sys.argv[1:])

    # If --all was passed, find the highest count specified and apply it to everything.
    if ALL_FLAG:
        MAX_COUNT = max(COUNT for _, COUNT in QUERIES)
        QUERIES = [(QUERY, MAX_COUNT) for QUERY, _ in QUERIES]

    for QUERY, COUNT in QUERIES:
        RESULTS = search(QUERY, COUNT)
        for LINE in RESULTS:
            print(LINE)