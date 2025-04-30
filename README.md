## [![Git](https://skillicons.dev/icons?i=git)](https://skillicons.dev) Credits

Inspired by [Bookmark](https://github.com/username/repository) by [@M00t3](https://github.com/M00t3).
# QuickSearch

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=macos" alt="macOS" />
  </a>
  <h3>A powerful, minimal bookmark launcher and search shortcut tool for macOS</h3>
  
  ![GitHub License](https://img.shields.io/github/license/YOUR_USERNAME/QuickSearch)
  ![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
</div>

Launch websites via abbreviations or search within predefined sources through Raycast. QuickSearch lets you access your favorite sites and search engines with just a few keystrokes.

## Requirements

[![Required Technologies](https://skillicons.dev/icons?i=macos,python)](https://skillicons.dev)

- macOS
- [Raycast](https://www.raycast.com/)
- Python 3.x

## Installation

### [![Bash](https://skillicons.dev/icons?i=bash)](https://skillicons.dev) Automatic Setup (Recommended)

```bash
bash <(curl -s https://raw.githubusercontent.com/YOUR_USERNAME/QuickSearch/main/install.sh)
```

This automatically configures everything including scripts and Raycast integration.

### [![Git](https://skillicons.dev/icons?i=git)](https://skillicons.dev) Manual Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/QuickSearch.git ~/QuickSearch
   ```

2. **Verify Python Installation**

   ```bash
   python3 --version
   ```

3. **Configure Settings**

   Edit `~/QuickSearch/config.ini`:

   ```ini
   [open_link]
   browser = safari

   [default]
   default_flag = quick-search
   use_rofi = false
   dwm_workspace = 2
   i3wm_workspace = 2
   ```

4. **Create Configuration Files**

   Create `~/.sites.txt`:
   ```
   https://chat.openai.com
   https://www.youtube.com
   ```

   Create `~/.quick_search.txt`:
   ```
   yt youtube.com
   ar wiki.archlinux.org
   ```

## Raycast Integration

1. **Enable Script Commands Directory**
   
   In Raycast: `Preferences → Extensions → Script Commands → Add Directory`

2. **Create Script Files**

   Place these in your Raycast script folder (e.g., `~/raycast-scripts/`):

   **qs.sh - Quick Search**

   ```bash
   #!/bin/bash

   # Required parameters:
   # @raycast.schemaVersion 1
   # @raycast.title qs
   # @raycast.mode compact
   # @raycast.argument1 { "type": "text", "placeholder": "Abbreviation" }
   # @raycast.argument2 { "type": "text", "placeholder": "Search term", "optional": true }

   # Optional parameters:
   # @raycast.icon 🔍

   python3 ~/QuickSearch/bookmark.py --quick-search "$1" "$2"
   ```

   **aqs.sh - Add Quick Site**

   ```bash
   #!/bin/bash

   # Required parameters:
   # @raycast.schemaVersion 1
   # @raycast.title aqs
   # @raycast.mode compact
   # @raycast.argument1 { "type": "text", "placeholder": "Abbreviation" }
   # @raycast.argument2 { "type": "text", "placeholder": "Full URL" }

   # Optional parameters:
   # @raycast.icon ➕

   python3 ~/QuickSearch/add_site.py "$1" "$2"
   ```

3. **Make Scripts Executable**

   ```bash
   chmod +x ~/raycast-scripts/qs.sh ~/raycast-scripts/aqs.sh
   ```

## Usage Examples

### [![Browser](https://skillicons.dev/icons?i=chrome)](https://skillicons.dev) Quick Search (`qs`)

Search YouTube for "linux tips":
```
qs yt linux tips
```
↳ Opens: `https://www.youtube.com/results?search_query=linux tips`

Open GitHub (if abbreviation exists):
```
qs gh
```
↳ Opens: `https://github.com`

### [![Markdown](https://skillicons.dev/icons?i=md)](https://skillicons.dev) Add Quick Site (`aqs`)

Add GitHub abbreviation:
```
aqs gh https://github.com
```
↳ Adds entry to configuration files

## Project Structure

```
QuickSearch/
│
├── bookmark.py             # Main script handling searches
├── add_site.py             # Script to add site abbreviations
├── quick_search_config.py  # Abbreviation dictionary
├── config.ini              # Configuration file
├── .sites.txt              # List of bookmarked URLs
├── .quick_search.txt       # Abbreviation to URL mappings
└── install.sh              # Automatic setup script
```

## [![Technologies](https://skillicons.dev/icons?i=linux,bash)](https://skillicons.dev) Features

- **Lightning-fast searches** - Launch websites with just a few keystrokes
- **Customizable abbreviations** - Create your own shortcuts for any website
- **Seamless integration** with Raycast
- **Minimal dependencies** - Just Python and Raycast required
- **Cross-browser support** - Configure your preferred browser

## [![Contribution](https://skillicons.dev/icons?i=github)](https://skillicons.dev) Contributing

Contributions are welcome! If you have ideas for:
- Additional search engines
- UI improvements
- New features

Please open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
