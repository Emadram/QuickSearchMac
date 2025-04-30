def sites_dict(query=None):
    return {
        "ar": f"https://wiki.archlinux.org/search/?q={query}" if query else "https://wiki.archlinux.org",
        "db": f"https://wiki.debian.org/search?keywords={query}" if query else "https://wiki.debian.org",
        "dh": f"https://devhints.io/?q={query}" if query else "https://devhints.io",
        "chi": "https://overapi.com",
        "chg": "https://cheatography.com",
        "gpt": "https://chat.openai.com/chat",
        "dt": "http://dotshare.it",
        "gt": "https://github.com",
        "dj": f"https://docs.djangoproject.com/en/5.0/search/?q={query}" if query else "https://docs.djangoproject.com/en/5.0/",
        "yt": f"https://www.youtube.com/results?search_query={query}" if query else "https://www.youtube.com",
        "std": f"https://emu.edu.tr",
        "go": f"https://google.com?{query}" if query else "https://google.com",
    }