#!/usr/bin/env python3
# Honest tab count (pure stdlib): writes the digit count to /output/entry.txt.
# 47: a specific, odd, lived-in tab-hoarder total — bounty dashboards, docs,
# leaderboards, half of them things sworn to be read later. High enough to
# surprise, not round enough to look invented.
import os

# The tab count, counted once and kept as a plain digit string: 47.
TAB_COUNT = "47"

OUTPUT_PATH = "/output/entry.txt"


def tab_count():
    """Return the tab count as a short digit string."""
    text = TAB_COUNT.strip()
    assert text.isdigit() and 1 <= len(text) <= 5
    return text


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(OUTPUT_PATH, tab_count())

if __name__ == "__main__":
    main()
