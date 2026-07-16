from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
from pathlib import Path


REDO_STEPS = [1, 3, 7, 14]
LOG_FILE = Path(__file__).with_name("mistake_log_template.csv")


def parse_iso_date(value: str) -> date | None:
    value = value.strip()
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def due_rows(rows: list[dict[str, str]], today: date) -> list[dict[str, str]]:
    due: list[dict[str, str]] = []
    for row in rows:
        redo_date = parse_iso_date(row.get("next_redo_date", ""))
        if redo_date is not None and redo_date <= today:
            due.append(row)
    return due


def next_redo_from_last_attempt(last_attempt: date | None, fails: int) -> date:
    if last_attempt is None:
        last_attempt = date.today()
    if fails <= 0:
        return last_attempt + timedelta(days=REDO_STEPS[0])
    step_index = min(fails, len(REDO_STEPS) - 1)
    return last_attempt + timedelta(days=REDO_STEPS[step_index])


def main() -> None:
    if not LOG_FILE.exists():
        print(f"Missing log file: {LOG_FILE}")
        return

    with LOG_FILE.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    today = date.today()
    due = due_rows(rows, today)
    print(f"Today: {today.isoformat()}")
    print(f"Due reviews: {len(due)}")

    for idx, row in enumerate(due, start=1):
        print(
            f"{idx}. {row.get('problem', '').strip()} "
            f"[{row.get('pattern', '').strip()}] "
            f"redo_by={row.get('next_redo_date', '').strip()}"
        )


if __name__ == "__main__":
    main()
