#!/usr/bin/env python3

import os
import subprocess
import time
import platform
import argparse
import configparser

from quick_search_config import sites_dict

# --- Load config.ini ---
script_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(script_dir, "config.ini")

config = configparser.ConfigParser()
config.read(config_path)

browser = config.get("open_link", "browser", fallback="safari").lower()
default_flag = config.get("default", "default_flag", fallback="open")
use_rofi = config.getboolean("default", "use_rofi", fallback=False)
dwm_workspace = config.get("default", "dwm_workspace", fallback="2")
i3wm_workspace = config.get("default", "i3wm_workspace", fallback="2")

# --- Workspace switching (Linux only) ---
def switch_workspace():
    if platform.system() != "Linux":
        return
    if subprocess.run(["pgrep", "i3"], stdout=subprocess.DEVNULL).returncode == 0:
        subprocess.run(["i3-msg", "workspace", i3wm_workspace], stdout=subprocess.DEVNULL)
    elif subprocess.run(["pgrep", "dwm"], stdout=subprocess.DEVNULL).returncode == 0:
        subprocess.run(["xdotool", "key", f"Super_L+{dwm_workspace}"], stdout=subprocess.DEVNULL)

# --- Open in browser based on config ---
def open_with_browser(url):
    if platform.system() == "Darwin":
        subprocess.run(["open", "-a", browser.capitalize(), url])
    else:
        subprocess.run([browser, url])

# --- Open site from .sites.txt ---
def open_site():
    sites_file = os.path.join(script_dir, ".sites.txt")
    with open(sites_file, "r") as f:
        lines = [line.strip() for line in f if not line.startswith("#") and line.strip()]
    lines_str = "\n".join(lines)

    if use_rofi:
        result = subprocess.run(["rofi", "-dmenu", "-i", "-p", "Choose site"],
                                input=lines_str, text=True, capture_output=True)
        selected = result.stdout.strip()
    else:
        proc = subprocess.Popen(["fzf"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        selected, _ = proc.communicate(lines_str)

    if selected in lines:
        open_with_browser(selected)
        time.sleep(0.3)
        switch_workspace()

# --- Quick search from .quick_search.txt ---
def quick_search(inputs=None):
    file_path = os.path.join(script_dir, ".quick_search.txt")

    if not inputs:
        if use_rofi:
            result = subprocess.run(["rofi", "-dmenu", "-i", "-p", "Search to:"],
                                    text=True, capture_output=True)
            inputs = result.stdout.strip().split()
        else:
            inputs = input("Search to: ").split()

    if not inputs:
        print("Usage: {abbreviation} {search query}")
        return

    first_part = inputs[0]
    search_to = " ".join(inputs[1:]) if len(inputs) > 1 else None

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Missing .quick_search.txt")
        return

    site_url = next((line.split()[1] for line in lines if line.startswith(first_part)), None)
    sites = sites_dict(search_to)

    if first_part in sites and search_to:
        open_with_browser(sites[first_part])
    elif site_url and search_to:
        open_with_browser(f"https://www.startpage.com/sp/search?query=site:{site_url} {search_to}")
    elif site_url:
        open_with_browser(site_url)
    else:
        print("No match found in quick search.")

    time.sleep(0.3)
    switch_workspace()

# --- Entry point ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--quick-search", action="store_true", help="Quick search with abbreviation")
    parser.add_argument("-o", "--open", action="store_true", help="Open from .sites.txt")
    parser.add_argument("input", nargs="*", help="Search input (e.g. yt music)")
    args = parser.parse_args()

    if args.quick_search:
        quick_search(inputs=args.input)
    elif args.open:
        open_site()
    elif default_flag == "quick-search":
        quick_search()
    elif default_flag == "open":
        open_site()
    else:
        print("No action specified.")