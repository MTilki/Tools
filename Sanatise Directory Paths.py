import os
import re

# Set a max length for path length if needed
MAX_PATH_LENGTH = 260

def sanitize_name(name):
    """
    Remove trailing spaces and replace spaces and special characters with underscores.
    """
    # Remove trailing spaces
    name = name.rstrip()
    # Replace spaces and special characters with underscores
    name = re.sub(r'[^\w\.-]', '_', name)
    return name

def sanitize_paths(root_dir):
    """
    Recursively sanitize all file and folder names in the given directory.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Sanitize files in the directory
        for filename in filenames:
            sanitized_name = sanitize_name(filename)
            old_path = os.path.join(dirpath, filename)
            new_path = os.path.join(dirpath, sanitized_name)

            if old_path != new_path:
                print(f"Renaming file: {old_path} -> {new_path}")
                os.rename(old_path, new_path)

        # Sanitize directories in the directory path
        for dirname in dirnames:
            sanitized_name = sanitize_name(dirname)
            old_path = os.path.join(dirpath, dirname)
            new_path = os.path.join(dirpath, sanitized_name)

            if old_path != new_path:
                print(f"Renaming folder: {old_path} -> {new_path}")
                os.rename(old_path, new_path)

        # Check path length and warn if it exceeds MAX_PATH_LENGTH
        if len(dirpath) > MAX_PATH_LENGTH:
            print(f"Warning: Path length exceeds {MAX_PATH_LENGTH} characters: {dirpath}")

# Specify the root directory to sanitize
root_directory = "/Documents/Uni 2"  # Change to your target directory

sanitize_paths(root_directory)
