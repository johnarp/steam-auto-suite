<div align="center">

![Banner](../assets/banner_art.png)

# Steam Auto Art

Automatically applies your custom Steam artwork to your library.

</div>

## How It Works

Steam stores all custom game artwork in one folder on your computer. Every image follows a specific naming convention tied to a game's App ID.

This script reads your organized artwork folders and copies everything to the right place automatically.

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

### 2. Organize Your Artwork

Place your artwork in folders named after each game's **App ID**. You can find a game's App ID on its Steam store page URL.

```
https://store.steampowered.com/app/[APP_ID]/Game_Name/
```

Alternatively, you can use [Steam Auto ID](../steam-auto-id/) to look them up by name.

Your folder structure should look like this:

```
📁 Steam Assets/
|--- 💽 SteamAutoApply.py
|--- 📁 1030300                     <-- App ID (Hollow Knight: Silksong)
    |--- 🖼️ 1030300p.png
    |--- 🖼️ 1030300_hero.png
    |--- 🖼️ 1030300_logo.png
    |--- 🖼️ 1030300.png
|--- 📁 2868840                     <-- App ID (Slay the Spire 2)
    |--- 🖼️ 2868840p.png
    |--- 🖼️ 2868840_hero.png
    |--- 🖼️ 2868840_logo.png
    |--- 🖼️ 2868840.png
|--- ...
```

### 3. Name Your Artwork Correctly

Each file must follow Steam's naming convention exactly, using the game's App ID.

| File Name | Art Type |
| - | - |
| `[ID]p.png` | Cover |
| `[ID]_hero.png` | Background |
| `[ID]_logo.png` | Logo |
| `[ID].png` | Wide Cover |

Replace `[ID]` with the actual App ID. For example, using `1030300` for Hollow Knight: Silksong:

```
1030300p.png
1030300_hero.png
1030300_logo.png
1030300.png
```

You do not need all of these. Include only the ones you have or want to include.

### 4. Edit the Script

Open `SteamAutoApply.py` in any text editor, such as Notepad, and find this line near the top:

```python
GRID_PATH = r"C:\Program Files (x86)\Steam\userdata\[YOUR USER ID]\config\grid"
```

Replace `[YOUR USER ID]` with your actual User ID from Step 1. For example:

```python
GRID_PATH = r"C:\Program Files (x86)\Steam\userdata\123456789\config\grid"
```

> **Installed Steam somewhere else?** Update the full path accordingly. For example: `D:\Steam\userdata\...`

## Running the Script

Make sure `SteamAutoApply.py` is in the **same folder** as all your App ID folders, then run it:

```
python SteamAutoApply.py
```

You'll see output like:

```
Assets: C:\Users\You\Desktop\Steam Auto Apply
Steam:  C:\Program Files (x86)\Steam\userdata\123456789\config\grid
 
[OK]: 1091500 --> 1091500p.png
[OK]: 1091500 --> 1091500_hero.png
[OVERWRITE]: 292030_hero.png
[OK]: 292030 --> 292030_hero.png
 
Done.
```

`[OK]` means the file was copied. `[OVERWRITE]` means a file with that name already existed in your Steam folder and was replaced.

## Bonus: Logo Placement and Scaling

Steam supports `.json` files alongside your artwork to control logo placement and scaling. For example:

```json
{
    "nVersion": 1,
    "logoPosition": {
        "pinnedPosition": "CenterCenter",
        "nWidthPct": 41.33,
        "nHeightPct": 100
    }
}
```

| Key | Values |
| - | - |
| `nVersion` | Format version. Keep as `1` |
| `pinnedPosition` | Where the logo is anchored. Options: `BottomLeft`, `TopCenter`, `CenterCenter`, `BottomCenter` |
| `nWidthPct` | Width of the logo in `%` |
| `nHeightPct` | Height of the logo in `%` |

> `"nVersion": 1` is just what Steam expects. You should keep it as `1`, as changing it doesn't change anything and may break compatibility.

### How To Use

Create a `.json` using the format above with your own values.

Place the `.json` file in the same folder as your artwork. Make sure it follows the naming convention: `[ID].json`. For example:

```
📁 Steam Assets/
|--- 💽 SteamAutoApply.py
|--- 📁 1030300                     <-- App ID (Hollow Knight: Silksong)
    |--- 🖼️ 1030300p.png
    |--- 🖼️ 1030300_hero.png
    |--- 🖼️ 1030300_logo.png
    |--- 🖼️ 1030300.png
    |--- ⚙️ 1030300.json
|--- ...
```

If you run into issues, try restarting Steam. If that doesn't work, try fully exiting Steam then running the script before reopening.

> Note: Steam may not always preserve or immediately apply `.json` layout changes. Behavior can be inconsistent, especially after updates or reapplying artwork.

## Notes

- You may need to **restart Steam** (or at least reload your library) after running the script for changes to appear.
- Running the script again will **overwrite any previously copied files.** This is intentional.
- Files that don't follow the naming convention won't break anything. They'll just be ignored by Steam.
- **Icons are not supported.** Steam stores them in a different folder and may overwrite them automatically. They are outside the scope of this tool.