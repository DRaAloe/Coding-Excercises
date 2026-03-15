


import random


def roll_die(sides: int = 6) -> int:
    """Roll a fair die with the given number of sides."""
    return random.randint(1, sides)


def main() -> None:
    print("6-sided dice roller. Press Enter to roll, or type 'q' to quit.")
    while True:
        user = input("Roll? [Enter/q] ").strip().lower()
        if user in {"q", "quit", "exit"}:
            print("Bye!")
            break
        result = roll_die()
        print(f"You rolled: {result}\n")


if __name__ == "__main__":
    main()
