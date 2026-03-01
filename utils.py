from prettytable import PrettyTable


def print_table(rows, headers):
    table = PrettyTable()
    table.field_names = headers
    for row in rows:
        table.add_row(row)
    print(table)


def print_separator(title=""):
    width = 64
    if title:
        print(f"\n{'=' * width}")
        print(title.center(width))
        print(f"{'=' * width}")
    else:
        print("=" * width)


def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def get_float_input(prompt, min_val=0.0):
    while True:
        try:
            value = float(input(prompt))
            if value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_str_input(prompt, max_length=None):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty.")
            continue
        if max_length and len(value) > max_length:
            print(f"Input must be at most {max_length} characters.")
            continue
        return value
