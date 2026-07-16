from __future__ import annotations

import subprocess
import sys
from pathlib import Path


FILES = [
    "01_best_time_stock_drill.py",
    "02_move_zeroes_drill.py",
    "03_is_subsequence_drill.py",
    "04_valid_parentheses_drill.py",
]


def main() -> None:
    base_dir = Path(__file__).parent
    for file_name in FILES:
        print(f"\n=== Running {file_name} ===")
        subprocess.run([sys.executable, str(base_dir / file_name)], check=False)


if __name__ == "__main__":
    main()
