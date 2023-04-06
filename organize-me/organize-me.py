import os
from pathlib import Path
from organize import SUBDIRECTORIES


def pick_directory(file_suffix):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == file_suffix:
                return category
    return "MISC"


def organize_directory():
    for item in os.scandir():
        if item.is_dir() or Path(item).suffix.lower() == ".py":
            continue
        path_file = Path(item)
        file_type = path_file.suffix.lower()
        directory = pick_directory(file_type)
        directory_path = Path(directory)
        if not directory_path.is_dir():
            directory_path.mkdir()
        path_file.rename(directory_path.joinpath(path_file))


organize_directory()