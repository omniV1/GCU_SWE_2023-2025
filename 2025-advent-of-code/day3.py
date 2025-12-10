"""Advent of Code 2025 - Day 3: Lobby (escalator batteries).
Puzzle recap:
- Each line is a bank of batteries (digits 1-9).
- You must turn on exactly two batteries in order (cannot reorder).
- The bank's joltage is the two-digit number formed by those picks.
- Goal: for each bank, find the maximum joltage; then sum across banks.

Your tasks (fill the TODOs):
1) Implement `max_bank_joltage(bank: str) -> int`:
   - Input: string of digits, length >= 2.
   - You must pick an index i for the tens digit and j>i for the ones digit.
   - Compute the two-digit number 10*bank[i]+bank[j], maximize it.
   - Return that maximum value.
   - Two ways:
       a) Simple double loop over all pairs (i,j) with i<j; track the max.
       b) Faster: build a suffix-max array of best trailing digit for each i,
          then scan once. Either is fine for learning.
2) Implement `total_output(path: Path) -> int` to sum max joltage per line.
3) Wire `main()` to read `day3_input.txt` (already placed) and print the sum.

Suggested test from the prompt (each should be the max per bank):
  987654321111111 -> 98
  811111111111119 -> 89
  234234234234278 -> 78
  818181911112111 -> 92
Sum = 357.
"""

from __future__ import annotations

from pathlib import Path


def max_bank_joltage(bank: str, k: int) -> int:
    """Return the maximum two-digit value achievable from a bank string.

    TODO: implement.
    Hints for double-loop version:
      best = -1
      for i in range(len(bank)-1):
          for j in range(i+1, len(bank)):
              value = 10*int(bank[i]) + int(bank[j])
              best = max(best, value)
      return best

    If you want the suffix-max approach instead:
      - Build suffix_max where suffix_max[i] = max digit from i..end.
      - Then for each i, best = max(best, 10*digit[i] + suffix_max[i+1]).
    """
    digits = [int(ch) for ch in bank.strip()]
    drop = len(digits) - k
    stack = []
    for d in digits:
        while stack and drop > 0 and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)
    best = stack[:k]
    return int("".join(map(str, best)))
    raise NotImplementedError


def total_output(path: Path, k: int) -> int:
    """Sum the maximum joltage from each non-empty line in the file."""
    # TODO: implement by reading lines, skipping blanks, summing max_bank_joltage.
    total = 0
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        total += max_bank_joltage(line, k)
    return total
    raise NotImplementedError


def main() -> None:
    # TODO: wire to day3_input.txt
    input_path = Path(__file__).with_name("day3_input.txt")
    print(total_output(input_path, k=12))


if __name__ == "__main__":
    main()
