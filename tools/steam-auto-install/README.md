<div align="center">

![Banner](../../assets/banner_install.png)

# Steam Auto Install

Automatically install Steam games from a list.

</div>

## How It Works

Steam has a built-in command line interface which supports triggering actions like installing and uninstalling games.

This script reads a list of App IDs from `install.json` and opens the Steam install dialog for each one automatically.

## Requirements

- Windows
- [Python3](https://www.python.org/downloads/) (Website) or [Python3](https://apps.microsoft.com/detail/9pnrbtzxmb4z) (Microsoft Store) installed

## Setup

Create a file called `install.json` in the same folder as `SteamAutoInstall.py`. List your games to install like this:

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

> **Keep Steam open before running.** You will need to manually confirm installs in the dialog box.

Make sure both `SteamAutoInstall.py` and `install.json` are in the **same folder,** then run:

```
python SteamAutoInstall.py
```

You'll see output like this:

```
[INSTALLING]: 367520
[INSTALLING]: 1030300
[INSTALLING]: 646570
[INSTALLING]: 2868840
```

## Notes

- **Always keep Steam open before running.**
- You will need to manually confirm through the pop-up dialog box to install the game.
    - Steam can only handle one game at a time. If a game's dialog box is supposed to open while the previous one is open, the current game is skipped.
    - To help mitigate this, there is a delay between installs, allowing you to have enough time to confirm an install before the other one arrives. You can change this value in `SteamAutoInstall.py` by looking for the `DELAY` variable and changing the number.
- App IDs must be integers in `install.json`, **not** wrapped in quotes: `1030300`, not `"1030300"`.