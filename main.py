"""A small interactive physics unit converter."""


def read_number(prompt):
    """Read a decimal number, repeating the prompt if the input is invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number (for example, 12 or 3.5).")


def format_number(number):
    """Display numbers without unnecessary trailing zeroes."""
    return f"{number:.6g}"


def convert(value, conversion):
    """Convert value using the selected conversion's function."""
    return conversion[2](value)


CONVERSIONS = {
    "length": [
        ("Centimeter", "Meter", lambda value: value / 100),
        ("Meter", "Centimeter", lambda value: value * 100),
        ("Kilometer", "Meter", lambda value: value * 1000),
        ("Meter", "Kilometer", lambda value: value / 1000),
    ],
    "time": [
        ("Second", "Hour", lambda value: value / 3600),
        ("Second", "Minute", lambda value: value / 60),
        ("Minute", "Second", lambda value: value * 60),
        ("Minute", "Hour", lambda value: value / 60),
        ("Day", "Minute", lambda value: value * 24 * 60),
    ],
    "velocity": [
        ("Meter/second", "Centimeter/second", lambda value: value * 100),
        ("Centimeter/second", "Meter/second", lambda value: value / 100),
        ("Kilometer/hour", "Meter/second", lambda value: value / 3.6),
        ("Meter/second", "Kilometer/hour", lambda value: value * 3.6),
    ],
    "force": [
        ("Newton", "Kilogram·meter/second²", lambda value: value),
        ("Kilogram·meter/second²", "Newton", lambda value: value),
        ("Newton", "Dyne", lambda value: value * 100_000),
        ("Dyne", "Newton", lambda value: value / 100_000),
    ],
}


def show_conversions(quantity):
    """Print the available conversions for one quantity."""
    print(f"\nConversions for {quantity.title()}:")
    for number, (source, target, _) in enumerate(CONVERSIONS[quantity], start=1):
        print(f"{number}. {source} to {target}")


def read_menu_choice(prompt, maximum):
    """Read an integer menu choice in the range 1..maximum."""
    while True:
        choice = input(prompt).strip()
        try:
            choice = int(choice)
        except ValueError:
            print(f"Enter a whole number from 1 to {maximum}.")
            continue

        if 1 <= choice <= maximum:
            return choice
        print(f"Choose a number from 1 to {maximum}.")


def main():
    print("=" * 48)
    print("          Physics Unit Converter")
    print("=" * 48)

    quantities = list(CONVERSIONS)
    while True:
        print("\nAvailable quantities:")
        for number, quantity in enumerate(quantities, start=1):
            print(f"{number}. {quantity.title()}")
        print("Q. Quit")

        selected = input("Choose a quantity: ").strip().lower()
        if selected == "q":
            print("Goodbye!")
            break

        try:
            quantity_number = int(selected)
            if not 1 <= quantity_number <= len(quantities):
                raise ValueError
            quantity = quantities[quantity_number - 1]
        except ValueError:
            print("Invalid choice. Select a listed number or Q to quit.")
            continue

        show_conversions(quantity)
        conversions = CONVERSIONS[quantity]
        conversion_number = read_menu_choice(
            f"Choose a conversion (1-{len(conversions)}): ", len(conversions)
        )
        conversion = conversions[conversion_number - 1]
        value = read_number(f"Enter the value in {conversion[0]}: ")
        result = convert(value, conversion)
        print(f"{format_number(value)} {conversion[0]} = "
              f"{format_number(result)} {conversion[1]}")


if __name__ == "__main__":
    main()
