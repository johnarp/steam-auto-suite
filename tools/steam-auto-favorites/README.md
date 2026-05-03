<div align="center">

![Banner](../../assets/banner_favorites.png)

# Steam Auto Favorites

Automatically populates your Steam favorites.

</div>

## How It Works

Steam stores your favorites in a config file on your computer.

This script reads a `favorites.json` file you define and writes your favorites directly into that config.

## Requirements

- Windows
- [Python3](https://www.python.org/downloads/) (Website) or [Python3](https://apps.microsoft.com/detail/9pnrbtzxmb4z) (Microsoft Store) installed

## Setup

### 1. Find Your Steam User ID

Open File Explorer and navigate to:

```
C:\Program Files (x86)\Steam\userdata
```

There will be a folder with a long number as its name. That's your User ID!

If there are multiple, open Steam and check which one was modified most recently.

### 2. Edit the Script

Open `SteamAutoFavorites.py` in any text editor, such as Notepad, and find this line near the top:

```python
CONFIG_PATH = r"C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\cloudstorage\cloud-storage-namespace-1.json"
```

Replace `[YOUR USER ID]` with your actual User ID from Step 1. For example:

```python
CONFIG_PATH = r"C:\Program Files (x86)\Steam\userdata\123456789\config\cloudstorage\cloud-storage-namespace-1.json"
```

> **Installed Steam somewhere else?** Update the full path accordingly. For example: `D:\Steam\userdata\...`

### 3. Create Your Favorites

Create a file called `favorites.json` in the same folder as `SteamAutoFavorites.py`. Define your favorites like this:

```json
[
	367520,
	1030300,
	2868840,
	1091500
]
```

Each entry is an App ID. You can use [Steam Auto ID](../steam-auto-id/) to find App IDs by name.

## Running the Script

> **Close Steam before running.** Steam may overwrite your changes if it's open.

Make sure both `SteamAutoFavorites.py` and `favorites.json` are in the **same folder,** then run:

```
python SteamAutoFavorites.py
```

You'll see output like this:

```
Backup saved: C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\cloudstorage\cloud-storage-namespace-1.json.backup

Created Favorites.
Done. Open Steam to see your Favorites.
```

`Created Favorites` means no favorites entry existed and one was created. `Updated Favorites` means a favorites entry existed and was overwritten.

## Notes

- **Always close Steam before running.** If Steam is open, it may sync its own version of the config and overwrite your changes.
- A backup of your config file is saved automatically before any changes are made. It will be at the same location as `cloud-storage-namespace-1.json`, named `cloud-storage-namespace-1.json.backup`. If something goes wrong and Steam is behaving strangely after running the script, here's how to restore it:
    1. Close Steam completely.
    2. Open File Explorer and navigate to the same folder as your `cloud-storage-namespace-1.json`. It will be at:
        ```
        C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\cloudstorage\
        ```
    3. Delete `cloud-storage-namespace-1.json`.
    4. Rename `cloud-storage-namespace-1.json.backup` to `cloud-storage-namespace-1.json`.
    5. Open Steam. Your collections and settings should be back to how they were before.
- Running the script again will **replace your favorites** with the ones in `favorites.json`. Any favorites not in your `favorites.json` will be removed.
- App IDs must be integers in `favorites.json`, **not** wrapped in quotes: `1030300`, not `"1030300"`.