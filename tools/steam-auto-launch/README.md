<div align="center">

![Banner](../../assets/banner_launch.png)

# Steam Auto Launch

Automatically applies launch options to your Steam games.

</div>

## How It Works

Steam stores your game settings, including launch options, in a config file on your computer.

This script reads a `launch_options.json` file you create and writes your launch options directly into that config.

## Requirements

- Windows
- [Python3](https://www.python.org/downloads/) (Website) or [Python3](https://apps.microsoft.com/detail/9pnrbtzxmb4z) (Microsoft Store) installed

## Setup

### 1. Find Your Steam User ID

Open File Explorer and navigate to

```
C:\Program Files (x86)\Steam\userdata
```

There will be a folder with a long number as its name. That's your User ID!

If there are multiple, open Steam and check which one was modified most recently.

### 2. Edit the Script

Open `SteamAutoLaunch.py` in any text editor, such as Notepad, and find this line near the top:

```python
GRID_PATH = r"C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\localconfig.vdf"
```

Replace `[YOUR USER ID]` with your actual User ID from Step 1. For example:

```python
GRID_PATH = r"C:\Program Files (x86)\Steam\userdata\123456789\config\localconfig.vdf"
```

> **Installed Steam somewhere else?** Update the full path accordingly. For example: `D:\Steam\userdata\...`

### 3. Create Your Launch Options

Create a file called `launch_options.json` in the same folder as `SteamAutoLaunch.py`. Define your launch options like this:

```json
{
    "2767030": "-novid -forcenovsync",
    "1808500": "-dx11"
}
```

Each key is an App ID and each value is the launch options string for that game. You can use [Steam Auto ID](../steam-auto-id/) to find App IDs by name.

## Running the Script

> **Close Steam before running.** Steam may overwrite your changes if it's open.

Make sure both `SteamAutoLaunch.py` and `launch_options.json` are in the **same folder,** then run:

```
python SteamAutoLaunch.py
```

You'll see output like this:

```
Backup saved: C:\Program Files (x86)\Steam\userdata[YOUR USER ID]\config\localconfig.vdf.backup

[OK]: 2767030 --> -novid -forcenovsync
[OK]: 1808500 --> -dx11

Done. Open Steam to see your launch options.
```

`[OK]` means the launch options were applied. `[NOT FOUND]` means the game has no entry in your config yet, which usually means it has never been launched. Launch it once through Steam and run the script again.

## Notes

- **Always close Steam before running.** If Steam is open, it may sync its own version of the config and overwrite your changes.
- A backup of your config file is saved automatically before any changes are made. It will be at the same location as `localconfig.vdf`, named `localconfig.vdf.backup`. If something goes wrong and Steam is behaving strangely after running the script, here's how to restore it:
    1. Close Steam completely.
    2. Open File Explorer and navigate to the same folder as your `localconfig.vdf`. It will be at:
        ```
        C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\
        ```
    3. Delete `localconfig.vdf`.
    4. Rename `localconfig.vdf.backup` to `localconfig.vdf`.
    5. Open Steam. Your settings should be back to how they were before.
- Running the script again will **replace existing launch options** for any App ID in your `launch_options.json`. Games not listed are left untouched.
- App IDs must be strings in `launch_options.json`, wrapped in quotes: `"553850"`, not `553850`.
- JSON does not allow trailing commas. Make sure the last entry in your `launch_options.json` has no comma after it.