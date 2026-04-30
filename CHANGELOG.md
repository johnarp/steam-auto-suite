# Changelog

[1.1.0]: https://github.com/johnarp/steam-auto-suite/releases/tag/v1.1.0
[1.0.0]: https://github.com/johnarp/steam-auto-suite/releases/tag/v1.0.0

## [1.1.0] - 2026-04-30

### General

#### Changed

- Added ✨ to indicate new tools
- A more general [disclaimer](./README.md/#disclaimer)

#### Fixed

- Corrected changelog entry for Steam Auto Collections 1.0.0

### Steam Auto Art

#### Added

- Documented support and instructions for `.json` logo positioning and scaling

### ✨ Steam Auto Name

#### Added

- Look up a Steam game's name by App ID
- Support for multiple IDs in a single command

## [1.0.0] - 2026-04-29

### ✨ Steam Auto Art

#### Added

- Automatically copies custom Steam artwork from organized local folders into Steam's grid directory
- Skips non-folder entries and non-numeric folder names automatically
- Warns on overwrite when a file with the same name already exists in the Steam grid folder
- Prints a per-file confirmation log on successful copy

### ✨ Steam Auto Collections

#### Added

- Creates and populates Steam collections from a user-defined collections.json
- Updates existing collections by name rather than duplicating them
- Automatically backs up cloud-storage-namespace-1.json before making any changes

### ✨ Steam Auto ID

#### Added

- Look up a Steam App ID by game name
- Support for multiple games in a single command