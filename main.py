#!/usr/bin/env python3
"""Hire Me In One Line — make.fun entry (program/v1).

Writes the entry text to /output/entry.txt.
"""
import os

ENTRY = """Give me a job and I'll ship it, test it, and tell you what broke before you find out."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)

if __name__ == "__main__":
    main()
