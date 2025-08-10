#!/usr/bin/env python
"""
Rename all .png files in a target directory to .jpg
without changing the file content.
"""

import os
from pathlib import Path

def rename_png_to_jpg(target_dir: str):
    """Rename all .png files in the given directory to .jpg."""
    directory = Path(target_dir)

    if not directory.exists():
        print(f"❌ Directory does not exist: {directory}")
        return

    count = 0
    for file_path in directory.glob("*.png"):
        new_path = file_path.with_suffix(".jpg")
        file_path.rename(new_path)
        print(f"🔄 {file_path.name}  →  {new_path.name}")
        count += 1

    print(f"✅ Rename complete: {count} file(s) changed.")

def main():
    # relative path to the illustrations directory
    target_directory = "assets/illustrations"
    rename_png_to_jpg(target_directory)

if __name__ == "__main__":
    main()
