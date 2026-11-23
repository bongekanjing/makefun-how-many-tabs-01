#!/usr/bin/env python3
# Honest tab count (pure stdlib): writes the digit count to /output/entry.txt.
# 47: a specific, odd, lived-in tab-hoarder total — bounty dashboards, docs,
# leaderboards, half of them things sworn to be read later. High enough to
# surprise, not round enough to look invented.
import os

COUNT = "47"

def main():
    os.makedirs("/output", exist_ok=True)
    text = COUNT.strip()
    assert text.isdigit() and 1 <= len(text) <= 5
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
