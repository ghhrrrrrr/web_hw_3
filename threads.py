import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def copy_file(file_path, target_dir):
    ext = file_path.suffix[1:]
    target_path = target_dir / ext / file_path.name
    target_path.parent.mkdir(parents=True, exist_ok=True) 
    shutil.copy2(file_path, target_path)

def process_directory(source_dir, target_dir, exec):
    with os.scandir(source_dir) as it:
        for entry in it:
            if entry.is_dir():
                exec.submit(process_directory, entry.path, target_dir, exec)
            elif entry.is_file():
                exec.submit(copy_file, Path(entry.path), target_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> <target_directory>")
        sys.exit(1)

    source_directory = Path(sys.argv[1])
    target_directory = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_directory.is_dir():
        print(f"Source directory '{source_directory}' does not exist or is not a directory.")
        sys.exit(1)

    with ThreadPoolExecutor(max_workers=6) as exec:
        process_directory(source_directory, target_directory, exec)
    
