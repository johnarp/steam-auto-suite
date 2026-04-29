# Changelog

[1.0.0]: https://github.com/johnarp/steam-auto-suite/releases/tag/v1.0.0

## [1.0.0] - 2026-04-29

### Steam Auto Art

#### Added

- Automatically copies custom Steam artwork from organized local folders into Steam's grid directory
- Skips non-folder entries and non-numeric folder names automatically
- Warns on overwrite when a file with the same name already exists in the Steam grid folder
- Prints a per-file confirmation log on successful copy

### Steam Auto Collections

#### Added

- Creates and populates Steam collections from a user-defined collections.json
- Updates existing collections by name rather than duplicating them
- Automatically backs up sharedconfig.vdf before making any changes

### Steam Auto ID

#### Added

- Look up a Steam App ID by game name
- Support for multiple games in a single command