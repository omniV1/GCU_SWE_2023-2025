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
    # TODO: implement this check.
    #
    # Hints:
    # - Convert to string s. If len(s) is odd, it can't be two equal halves.
    # - Split s into two equal halves; compare.
    # - Leading zeros are not allowed in input, so "0101" won't appear.
    raise NotImplementedError


def iter_invalid_ids(rng: Range) -> Iterator[int]:
    """Yield invalid IDs within a range (inclusive)."""
    # TODO: naive approach is to loop from rng.start to rng.end and test.
    # That may be fine if ranges are small; if ranges are large, think about
    # generating candidates of the form XYXY within bounds instead.
    raise NotImplementedError


def sum_invalid_ids(ranges: Iterable[Range]) -> int:
    """Sum all invalid IDs across ranges."""
    total = 0
    for rng in ranges:
        for n in iter_invalid_ids(rng):
            total += n
    return total


def main() -> None:
    # TODO: wire this to your actual puzzle input file (see day2_input.txt).
    # For now, this is a placeholder sample block; replace or keep for tests.
    sample = (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
        "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
        "824824821-824824827,2121212118-2121212124"
    )
    ranges = parse_ranges(sample)
    # When you're ready, compute:
    # print(sum_invalid_ids(ranges))
    print("Scaffold ready. Fill in TODOs, then run with your input.")


if __name__ == "__main__":
    main()
