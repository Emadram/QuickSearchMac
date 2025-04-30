# QuickSearch

<div align="center">
  <img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS" />
  <h3>A powerful, minimal bookmark launcher and search shortcut tool for macOS</h3>
  
  ![GitHub License](https://img.shields.io/github/license/YOUR_USERNAME/QuickSearch)
  ![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
</div>

Launch websites via abbreviations or search within predefined sources through Raycast. QuickSearch lets you access your favorite sites and search engines with just a few keystrokes.

## ![](https://img.shields.io/badge/REQUIREMENTS-7A7A7A?style=for-the-badge)

![](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)
![](https://img.shields.io/badge/Raycast-191919?style=for-the-badge)
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ![](https://img.shields.io/badge/INSTALLATION-7A7A7A?style=for-the-badge)

### ![](https://img.shields.io/badge/AUTOMATIC-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

```bash
bash <(curl -s https://raw.githubusercontent.com/YOUR_USERNAME/QuickSearch/main/install.sh)
```

This automatically configures everything including scripts and Raycast integration.

### ![](https://img.shields.io/badge/MANUAL-F05032?style=for-the-badge&logo=git&logoColor=white)

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

## ![](https://img.shields.io/badge/RAYCAST_INTEGRATION-191919?style=for-the-badge)

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

## ![](https://img.shields.io/badge/USAGE_EXAMPLES-0175C2?style=for-the-badge)

### ![](https://img.shields.io/badge/QUICK_SEARCH-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)

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

### ![](https://img.shields.io/badge/ADD_SITE-512BD4?style=for-the-badge&logo=bookmark&logoColor=white)

Add GitHub abbreviation:
```
aqs gh https://github.com
```
↳ Adds entry to configuration files

## ![](https://img.shields.io/badge/PROJECT_STRUCTURE-7A7A7A?style=for-the-badge)

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

## ![](https://img.shields.io/badge/FEATURES-00C7B7?style=for-the-badge)

- **Lightning-fast searches** - Launch websites with just a few keystrokes
- **Customizable abbreviations** - Create your own shortcuts for any website
- **Seamless integration** with Raycast
- **Minimal dependencies** - Just Python and Raycast required
- **Cross-browser support** - Configure your preferred browser

## ![](https://img.shields.io/badge/CONTRIBUTING-181717?style=for-the-badge&logo=github&logoColor=white)

Contributions are welcome! If you have ideas for:
- Additional search engines
- UI improvements
- New features

Please open an issue or submit a pull request.

## ![](https://img.shields.io/badge/LICENSE-FE7D37?style=for-the-badge)

This project is open source and available under the [MIT License](LICENSE).

## ![](https://img.shields.io/badge/CREDITS-F05032?style=for-the-badge&logo=git&logoColor=white)

Inspired by [Bookmark](https://github.com/M00t3/bookmark) by [@M00t3](https://github.com/M00t3).
