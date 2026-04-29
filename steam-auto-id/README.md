<div align="center">

![Banner](../assets/banner_id.png)

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

## Notes

- Capitalization, punctuation, and special characters don't matter. Steam's search handles it.
- Results are based on Steam's own store search. The top result may occasionally not be what you expected. Try a more specific name if that happens.