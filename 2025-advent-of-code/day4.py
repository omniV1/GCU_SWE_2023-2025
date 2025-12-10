"""Advent of Code 2025 - Day 4: Printing Department.

What we're counting:
- Grid of '.' (empty) and '@' (rolls of paper).
- A roll is reachable by a forklift if it has FEWER than 4 neighboring rolls
  in the 8 surrounding squares (N, NE, E, SE, S, SW, W, NW).
- Goal: count how many rolls meet that rule.

How to run:
  python day4.py               # uses day4_input.txt in this folder
  python day4.py --sample      # runs the 10x10 example, should print 13
  python day4.py --input path  # point at any other grid file

The code is intentionally plain loops so it reads like CS101 Python.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List
from collections import deque

Grid = List[str]

# 8 neighbor offsets around a cell.
DELTAS: list[tuple[int, int]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

# Example from the story; expected reachable count is 13.
SAMPLE_GRID = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]


def read_grid(path: Path) -> Grid:
    """Read the puzzle input file into a list of row strings."""
    rows: Grid = []
    for raw in path.read_text().splitlines():
        row = raw.strip()
        if row:
            rows.append(row)
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def neighbor_count(grid: Grid, r: int, c: int) -> int:
    """Count how many neighboring cells contain rolls ('@')."""
    count = 0
    for dr, dc in DELTAS:
        rr, cc = r + dr, c + dc
        if rr < 0 or cc < 0:
            continue
        if rr >= len(grid) or cc >= len(grid[rr]):
            continue
        if grid[rr][cc] == "@":
            count += 1
    return count


def neighbors(grid: Grid, r: int, c: int):
    """Yield valid neighbor coordinates around (r, c)."""
    for dr, dc in DELTAS:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(grid) and 0 <= cc < len(grid[rr]):
            yield rr, cc


def reachable_rolls(grid: Grid) -> int:
    """Return the number of rolls a forklift can reach (neighbor count < 4)."""
    total = 0
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "@":
                continue
            if neighbor_count(grid, r, c) < 4:
                total += 1
    return total


def solve(path: Path) -> int:
    """Load a grid file and count reachable rolls."""
    grid = read_grid(path)
    return reachable_rolls(grid)


# ----------------------------
# Part 2 helper scaffolding
# ----------------------------
def build_neighbor_counts(grid: Grid) -> list[list[int]]:
    """Precompute neighbor counts for every cell (used by cascade removal)."""
    counts: list[list[int]] = []
    for r, row in enumerate(grid):
        row_counts: list[int] = []
        for c, ch in enumerate(row):
            row_counts.append(neighbor_count(grid, r, c) if ch == "@" else 0)
        counts.append(row_counts)
    return counts


def cascade_removal_count(grid: list[list[str]]) -> int:
    """TODO: implement Part 2 (total rolls removed after repeated access).

    Recipe (one possible approach):
      1) Convert the grid to a mutable list of lists so you can set cells to '.'.
      2) Build neighbor counts via build_neighbor_counts(grid).
      3) Seed a queue/stack with all '@' cells whose count < 4.
      4) Pop a cell:
           - If it's still '@' and count < 4: remove it (set to '.'),
             increment answer, and for each neighbor that is '@':
                 * decrement its neighbor count
                 * if that neighbor's count just dropped below 4, enqueue it
      5) Repeat until the queue is empty; return the answer.

    Tip: only enqueue neighbors when you actually removed a roll.
    """
    rows, cols = len(grid), len(grid[0])

    def count_at(r, c) -> int:
        cnt = 0
        for dr, dc in DELTAS:
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == "@":
                cnt += 1
        return cnt

    counts = [
        [count_at(r, c) if grid[r][c] == "@" else 0 for c in range(cols)]
        for r in range(rows)
    ]

    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@" and counts[r][c] < 4:
                q.append((r, c))
    removed = 0

    while q:
        r, c = q.popleft()
        if grid[r][c] != "@":
            continue
        if counts[r][c] >= 4:
            continue

        grid[r][c] = "."
        removed += 1

        for dr, dc in DELTAS:
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == "@":
                counts[rr][cc] -= 1
                if counts[rr][cc] == 3:
                    q.append((rr, cc))

    return removed

    raise NotImplementedError("Fill in the cascade removal logic.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Count reachable rolls of paper.")
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        default=Path(__file__).with_name("day4_input.txt"),
        help="Path to the puzzle input grid (defaults to day4_input.txt).",
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Use the 10x10 example from the prompt; expected answer is 13.",
    )
    parser.add_argument(
        "--part2",
        action="store_true",
        help="Run the repeated-removal logic (you need to implement it first).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.sample:
        grid = SAMPLE_GRID
    else:
        grid = read_grid(args.input)

    if args.part2:
        mutable = [list(row) for row in grid]
        print(cascade_removal_count(mutable))
        return

    print(reachable_rolls(grid))


if __name__ == "__main__":
    main()
