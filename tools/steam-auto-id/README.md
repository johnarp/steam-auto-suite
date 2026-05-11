<div align="center">

![Banner](../../assets/banner_id.png)

# Steam Auto ID

Find a Steam game's App ID by name.

</div>

## How It Works

Steam has their own search endpoint link. It's like going to the Steam store and searching up the name of a game.

This script takes the names you provide and queries the endpoint. It returns the App ID and name of the top result for each name.

## Requirements

- [Python3](https://www.python.org/downloads/) (Website) or [Python3](https://apps.microsoft.com/detail/9pnrbtzxmb4z) (Microsoft Store) installed
- The `requests` Python library

## Setup

Open a terminal, such as Command Prompt or Powershell, and run:

```
pip install requests
```

This is needed to make web requests.

## Running the Script

Open a terminal and run:

```
python SteamAutoID.py "game name"
```

You can look up multiple names at once. For example:

```
python SteamAutoID.py "Hollow Knight: Silksong" "slay the spire 2" "cyberpunk"
```

You'll see output like:
```
1030300 - Hollow Knight: Silksong
2868840 - Slay the Spire 2
1091500 - Cyberpunk 2077
```

## Bonus: More Results

You can use `-#` to the right of a game name to specify how many results you want to see for that game. You can also use `--all` to apply the largest `-#` to every game name in the query.

Examples:

```
python SteamAutoID.py "wolfenstein" -3

612880 - Wolfenstein II: The New Colossus
201810 - Wolfenstein: The New Order
350080 - Wolfenstein: The Old Blood
```

```
python SteamAutoID.py "resident evil" -5 "hollow knight"

304240 - Resident Evil
2050650 - Resident Evil 4
952060 - Resident Evil 3
883710 - Resident Evil 2
21690 - Resident Evil 5
367520 - Hollow Knight
```

```
python SteamAutoID.py "god of war" "hollow knight" -2 --all

1593500 - God of War
2322010 - God of War Ragnarök
367520 - Hollow Knight
1030300 - Hollow Knight: Silksong
```

## Notes

- Capitalization, punctuation, and special characters don't matter. Steam's search handles it.
- Results are based on Steam's own store search. The top result may occasionally not be what you expected. Try a more specific name if that happens.