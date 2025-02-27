import os

def check_directory(path):
    """Checks if directory exists, creates if not."""
    if not os.path.exists(path):
        os.makedirs(path)
