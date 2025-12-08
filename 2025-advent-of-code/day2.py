"""Scaffold for Advent of Code Day 2 (invalid repeated IDs).

Goal (as I understand it):
- Each input token is a range like "11-22".
- A number is "invalid" if it is exactly two copies of the same digit sequence
  back-to-back (e.g., 55, 6464, 123123). No leading zeros allowed.
- Sum all invalid IDs that fall inside the given ranges.

This file is intentionally a scaffold for learning:
- Fill in the TODOs yourself.
- Keep the helper `is_invalid_id` small and easy to reason about.
- Prefer math/string reasoning over brute force full-range expansion
  (some ranges could be large).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator, List, Tuple


@dataclass
class Range:
    start: int
    end: int

    def __post_init__(self) -> None:
        if self.end < self.start:
            raise ValueError(f"Bad range: {self.start}-{self.end}")


def parse_ranges(text: str) -> List[Range]:
    """Parse comma-separated ranges like '11-22,95-115' into Range objects."""
    parts = [p.strip() for p in text.split(",") if p.strip()]
    result: List[Range] = []
    for part in parts:
        lo_hi = part.split("-")
        if len(lo_hi) != 2:
            raise ValueError(f"Bad range token: {part!r}")
        lo, hi = map(int, lo_hi)
        result.append(Range(lo, hi))
    return result


def is_invalid_id(n: int) -> bool:
    """Return True if n is exactly two copies of some digit sequence."""
    s = str(n)
    L = len(s)
    for c in range(1, L // 2 + 1):
        if L % c != 0:
            continue
        chunk = s[:c]
        k = L // c
        if k >= 2 and chunk * k == s:
            return True
    return False


def iter_invalid_ids(rng: Range) -> Iterator[int]:
    """Yield invalid IDs within a range (inclusive)."""
    for n in range(rng.start, rng.end + 1):
        if is_invalid_id(n):
            yield n


def sum_invalid_ids(ranges: Iterable[Range]) -> int:
    """Sum all invalid IDs across ranges."""
    total = 0
    for rng in ranges:
        for n in iter_invalid_ids(rng):
            total += n
    return total


def main() -> None:
    with open("day2_input.txt", "r", encoding="utf-8") as f:
        text = f.read().strip()
    ranges = parse_ranges(text)
    print(sum_invalid_ids(ranges))


if __name__ == "__main__":
    main()
