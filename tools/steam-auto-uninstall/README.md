<div align="center">

![Banner](../../assets/banner_uninstall.png)

# Steam Auto Uninstall

Automatically uninstall Steam games from a list.

</div>

## How It Works

Steam has a built-in command line interface which supports triggering actions like installing and uninstalling games.

This script reads a list of App IDs from `uninstall.json` and opens the Steam uninstall dialog for each one automatically.

## Requirements

- Windows
- [Python3](https://www.python.org/downloads/) (Website) or [Python3](https://apps.microsoft.com/detail/9pnrbtzxmb4z) (Microsoft Store) installed

## Setup

Create a file called `uninstall.json` in the same folder as `SteamAutoUninstall.py`. List your games to uninstall like this:

```json
[
    367520,
    1030300,
    646570,
    2868840
]
```

Each entry is an App ID. You can use [Steam Auto ID](../steam-auto-id/) to find App IDs by name.

## Running the Script

> **Keep Steam open before running.** You will need to manually confirm uninstalls in the dialog box.

Make sure both `SteamAutoUninstall.py` and `uninstall.json` are in the **same folder,** then run:

```
python SteamAutoUninstall.py
```

You'll see output like this:

```
[UNINSTALLING]: 367520
[UNINSTALLING]: 1030300
[UNINSTALLING]: 646570
[UNINSTALLING]: 2868840
```

## Notes

- **Always keep Steam open before running.**
- You will need to manually confirm through the pop-up dialog box to uninstall the game.
    - Steam can only handle one game at a time. If a game's dialog box is supposed to open while the previous one is open, the current game is skipped.
    - To help mitigate this, there is a delay between uninstalls, allowing you to have enough time to confirm an uninstall before the other one arrives. You can change this value in `SteamAutoUninstall.py` by looking for the `DELAY` variable and changing the number.
- App IDs must be integers in `uninstall.json`, **not** wrapped in quotes: `1030300`, not `"1030300"`.