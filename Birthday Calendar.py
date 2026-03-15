

from __future__ import annotations

import json
import os
import random
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Optional


DATA_FILENAME = "birthdays.json"
DATE_FORMAT = "%Y-%m-%d"  # ISO format (e.g. 2026-03-15)


def get_data_path() -> Path:
    return Path(__file__).resolve().parent / DATA_FILENAME


def load_birthdays() -> List[Dict[str, str]]:
    path = get_data_path()
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except Exception:
        pass
    return []


def save_birthdays(entries: List[Dict[str, str]]) -> None:
    path = get_data_path()
    with path.open("w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


def parse_date(value: str) -> Optional[date]:
    try:
        return datetime.strptime(value.strip(), DATE_FORMAT).date()
    except ValueError:
        return None


def format_entry(entry: Dict[str, str]) -> str:
    return f"{entry['name']} — {entry['date']}"


def sort_by_date(entries: List[Dict[str, str]]) -> List[Dict[str, str]]:
    def key_fn(e: Dict[str, str]) -> date:
        d = parse_date(e.get("date", ""))
        return d or date.min

    return sorted(entries, key=key_fn)


def sort_by_name(entries: List[Dict[str, str]]) -> List[Dict[str, str]]:
    return sorted(entries, key=lambda e: e.get("name", "").lower())


def randomize_birthdays(entries: List[Dict[str, str]], year: int = None) -> None:
    """Randomly assigns a birthday (month/day) for each entry.

    If year is provided, uses that year; otherwise uses current year.
    """
    if year is None:
        year = date.today().year

    for entry in entries:
        # Generate a random day in the year
        start = date(year, 1, 1).toordinal()
        end = date(year, 12, 31).toordinal()
        random_day = date.fromordinal(random.randint(start, end))
        entry["date"] = random_day.strftime(DATE_FORMAT)


def print_entries(entries: List[Dict[str, str]], title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    if not entries:
        print("(no birthdays stored yet)")
        return
    for idx, entry in enumerate(entries, start=1):
        print(f"{idx:2d}. {format_entry(entry)}")


def prompt(msg: str, default: Optional[str] = None) -> str:
    if default:
        return input(f"{msg} [{default}]: ").strip() or default
    return input(f"{msg}: ").strip()


def add_birthday(entries: List[Dict[str, str]]) -> None:
    name = prompt("Enter name").strip()
    if not name:
        print("Name cannot be empty.")
        return

    raw_date = prompt(f"Enter birthday ({DATE_FORMAT})")
    parsed = parse_date(raw_date)
    if not parsed:
        print(f"Invalid date format. Use {DATE_FORMAT}.")
        return

    entries.append({"name": name, "date": parsed.strftime(DATE_FORMAT)})
    save_birthdays(entries)
    print("Added.")


def remove_birthday(entries: List[Dict[str, str]]) -> None:
    if not entries:
        print("No entries to remove.")
        return
    print_entries(entries, "Current birthdays")
    choice = prompt("Enter number to remove (or blank to cancel)")
    if not choice:
        return
    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(entries):
        print("Number out of range.")
        return
    removed = entries.pop(idx)
    save_birthdays(entries)
    print(f"Removed: {format_entry(removed)}")


def main_menu() -> None:
    entries = load_birthdays()

    while True:
        print("\nBirthday Calendar")
        print("===============")
        print("1) List all birthdays (sorted by date)")
        print("2) List all birthdays (sorted by name)")
        print("3) Add a birthday")
        print("4) Remove a birthday")
        print("5) Randomly update stored birthdays")
        print("6) Exit")

        choice = prompt("Choose an option")
        if choice == "1":
            print_entries(sort_by_date(entries), "Birthdays (earliest to latest)")
        elif choice == "2":
            print_entries(sort_by_name(entries), "Birthdays (by name)")
        elif choice == "3":
            add_birthday(entries)
        elif choice == "4":
            remove_birthday(entries)
        elif choice == "5":
            year_input = prompt("Randomize for year (leave blank for current year)")
            if year_input:
                if not year_input.isdigit():
                    print("Year must be a number.")
                    continue
                year = int(year_input)
            else:
                year = None
            randomize_birthdays(entries, year=year)
            save_birthdays(entries)
            print("Birthdays have been randomly updated.")
        elif choice == "6":
            print("Goodbye!")
            return
        else:
            print("Unknown option. Please choose 1-6.")


if __name__ == "__main__":
    main_menu()
