from __future__ import annotations

import subprocess
import sys
from pathlib import Path


FILES = [
    "hash_pattern_lab.py",
    "00_hashing_bootcamp_drills.py",
    "01_hashing_variants.py",
    "02_sliding_window_variants.py",
    "03_intervals_greedy_variants.py",
    "04_graph_grid_variants.py",
    "05_heap_binary_search_variants.py",
    "06_amazon_style_story_variants.py",
    "07_amazon_common_problems.py",
    "08_amazon_hard_problems.py",
]


def main() -> None:
    base_dir = Path(__file__).parent
    for file_name in FILES:
        print(f"\n=== Running {file_name} ===")
        subprocess.run([sys.executable, str(base_dir / file_name)], check=False)


if __name__ == "__main__":
    main()
