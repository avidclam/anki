import sys
from pathlib import Path
from src.main import main

if __name__ == "__main__":
    top_dir = Path(__file__).parent

    try:
        error_message = main(top_dir)
        if error_message:
            print(error_message)
    except Exception as e:
        print(f"{e}", file=sys.stderr)
