from __future__ import annotations

import subprocess
import sys
from pathlib import Path


FILES = [
    "01_richest_customer_drill.py",
    "02_max_consecutive_ones_drill.py",
    "03_valid_palindrome_drill.py",
]


def main() -> None:
    base_dir = Path(__file__).parent
    for file_name in FILES:
        target = base_dir / file_name
        print(f"\n=== Running {file_name} ===")
        subprocess.run([sys.executable, str(target)], check=False)


if __name__ == "__main__":
    main()
