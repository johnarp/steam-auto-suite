<div align="center">

![Banner](../../assets/banner_name.png)

# Steam Auto Name

Find a Steam game's name by App ID.

</div>

## How It Works

Steam has their own details endpoint link. Given an App ID, it returns all the information Steam has about that app.

This script takes the IDs you provide, queries the endpoint, and returns the name of each one.

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
python SteamAutoName.py [app id]
```

You can look up multiple IDs at once. For example:

```
python SteamAutoName.py 1030300 2868840 1091500
```

You'll see output like:
```
1030300 - Hollow Knight: Silksong
2868840 - Slay the Spire 2
1091500 - Cyberpunk 2077
```

## Notes

- This is the reverse of [Steam Auto ID](../steam-auto-id/), which looks up an ID by name.
- If an ID doesn't exist or cannot be found, the script will let you know and continue with the rest.