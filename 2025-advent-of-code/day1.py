"""Dial demo for Advent of Code Day 1.

Kid-friendly version:
- Numbers go around a circle. Default is 0-99, starting at 50.
- Each move card is like "L10" or "R3".
- After every move, if we land on 0 we yell "DING!" and add 1 to the score.

Run examples:
  python day1.py --sample          # use the short story sample
  python day1.py --file input.txt  # read your full puzzle list
  python day1.py                   # paste moves by hand, end with a blank line

Helpful flags:
  --delay 0.0      turn off the animation pause
  --dial-size 10   shrink the dial to 0-9 for easier mental math
  --start 5        change the starting position
"""

from __future__ import annotations

import argparse
import sys
import time
from typing import Iterable, List, Tuple

Move = Tuple[str, int]


def parse_moves(lines: Iterable[str]) -> List[Move]:
    """Parse lines like 'L10' or 'R3' into a list of (direction, steps)."""
    moves: List[Move] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        direction = line[0].upper()
        if direction not in ("L", "R"):
            raise ValueError(f"Bad direction in move: {line!r}")
        try:
            steps = int(line[1:])
        except ValueError as exc:
            raise ValueError(f"Bad step count in move: {line!r}") from exc
        moves.append((direction, steps))
    return moves


def apply_move(position: int, move: Move, dial_size: int) -> int:
    """Return new position after applying one move on a dial."""
    direction, steps = move
    delta = steps if direction == "R" else -steps
    return (position + delta) % dial_size


def count_hits(position: int, move: Move, dial_size: int, mode: str) -> tuple[int, int]:
    """Return (zero_hits_from_this_move, new_position)."""
    new_pos = apply_move(position, move, dial_size)
    if mode == "end":
        return (1 if new_pos == 0 else 0, new_pos)

    direction, steps = move
    if direction == "R":
        hits = (position + steps) // dial_size
    else:
        if position == 0:
            hits = steps // dial_size
        elif steps < position:
            hits = 0
        else:
            hits = (steps - position) // dial_size + 1
    return (hits, new_pos)


def animate(
    moves: List[Move],
    *,
    start: int = 50,
    dial_size: int = 100,
    delay: float = 0.2,
    mode: str = "end",
) -> int:
    """Animate the moves and count how many times we land on 0."""
    position = start
    zero_hits = 0

    print(f"\nDial size: {dial_size} numbers (0 to {dial_size - 1})")
    print(f"Starting at: {position}\n")

    for idx, move in enumerate(moves, start=1):
        hits, position = count_hits(position, move, dial_size, mode)
        zero_hits += hits
        line = f"{idx:>3}. {move[0]}{move[1]:<4} -> {position:>3}"
        if hits:
            line += f"   DING x{hits}!"
        print(line)
        time.sleep(delay)

    print(f"\nTotal times on 0: {zero_hits}")
    return zero_hits

def read_moves_from_stdin() -> List[Move]:
    """Prompt the user to paste moves; stop on a blank line."""
    print("Paste your moves (one per line). End with a blank line.\n")
    lines = []
    for line in sys.stdin:
        if not line.strip():
            break
        lines.append(line)
    return parse_moves(lines)


def sample_moves() -> List[Move]:
    """The short example from the story; expected zero count is 3."""
    example = """
    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82
    """
    return parse_moves(example.strip().splitlines())


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Animate the dial moves.")
    parser.add_argument(
        "--file",
        "-f",
        help="Path to a file with one move per line (e.g., input.txt).",
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Use the built-in short example (lands on 0 three times).",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.25,
        help="Pause (seconds) between steps; set to 0 for instant.",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=50,
        help="Starting position on the dial.",
    )
    parser.add_argument(
        "--dial-size",
        type=int,
        default=100,
        help="How many numbers are on the dial (default 100 for 0-99).",
    )
    parser.add_argument(
        "--mode",
        choices=["end", "clicks"],
        default="end",
        help="Count only final zeros ('end') or every click on zero ('clicks').",
    )

    args = parser.parse_args(argv)

    if args.sample and args.file:
        parser.error("Choose either --sample or --file, not both.")

    if args.sample:
        moves = sample_moves()
    elif args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                moves = parse_moves(f)
        except FileNotFoundError:
            parser.error(f"File not found: {args.file}")
    else:
        moves = read_moves_from_stdin()

    animate(
        moves,
        start=args.start,
        dial_size=args.dial_size,
        delay=args.delay,
        mode=args.mode,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
