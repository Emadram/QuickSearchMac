
## Credits

Inspired by [Bookmark](https://github.com/M00t3/bookmark) by [@M00t3](https://github.com/M00t3).

<hr>

# QuickSearch
<div align="center">
  <img src="https://skillicons.dev/icons?i=macos" alt="macOS" />
  <h3>A powerful, minimal bookmark launcher and search shortcut tool for macOS</h3>
  
  ![GitHub License](https://img.shields.io/github/license/Emadram/QuickSearchMac)
  ![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
</div>

Launch websites via abbreviations or search within predefined sources through Raycast. QuickSearch lets you access your favorite sites and search engines with just a few keystrokes.

## Requirements

- macOS
- [Raycast](https://www.raycast.com/)
- Python 3.x

## Installation

### Automatic Setup (Recommended)

```bash
bash <(curl -s https://raw.githubusercontent.com/YOUR_USERNAME/QuickSearch/main/install.sh)
```

This automatically configures everything including scripts and Raycast integration.

### Manual Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/QuickSearch.git ~/QuickSearch
   ```

2. **Verify Python Installation**

   ```bash
   python3 --version
   ```
   
   No additional Python packages are required.

3. **Configuration Files**

   All necessary configuration files are included in the repository:
   
   - `config.ini`: Contains browser and environment settings
   - `.sites.txt`: Default bookmarked URLs
   - `.quick_search.txt`: Default abbreviation mappings
   
   These files will be automatically set up during installation. You can modify them later according to your preferences.

## Raycast Integration

1. **Create Script **
   
   In Raycast: `creat script command`
<img width="749" alt="1" src="https://github.com/user-attachments/assets/4eb39d23-3856-4dd6-ac7e-a44967ab1387" />
<img width="750" alt="2" src="https://github.com/user-attachments/assets/99513d60-62bf-4a33-b74d-5bedc52ae95f" />
Save them in the current Dir(folder) of the repo.

2. **Update Script Files**

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

   python3 ~/QuickSearchMac/bookmark.py --quick-search "$1" "$2"
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

   python3 ~/QuickSearchMac/add_site.py "$1" "$2"
   ```

4. **Make Scripts Executable**

   ```bash
   chmod +x ~/raycast-scripts/qs.sh ~/raycast-scripts/aqs.sh
   ```

## Usage Examples
<img width="747" alt="3" src="https://github.com/user-attachments/assets/841e8a0f-2513-4afa-903e-c2f6f31fc949" />
<img width="751" alt="4" src="https://github.com/user-attachments/assets/2ac5e2fa-1876-4db8-bce0-71dd0fb274b3" />


## Usage Examples without Raycast

### Quick Search (`qs`)

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

### Add Quick Site (`aqs`)

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

## Features

- **Lightning-fast searches** - Launch websites with just a few keystrokes
- **Customizable abbreviations** - Create your own shortcuts for any website
- **Seamless integration** with Raycast
- **Minimal dependencies** - Just Python and Raycast required
- **Cross-browser support** - Configure your preferred browser

## Contributing

Contributions are welcome! If you have ideas for:
- Additional search engines
- UI improvements
- New features

Please open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
