from pathlib import Path

def check_and_create_dir(dir):
    Path(dir).mkdir(parents=True, exist_ok=True)