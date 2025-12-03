from helpers import read_file


def find_max_joltage(bank: str) -> int:

    # Set the 10s position to the first character, and 1s position to -1 so it'll be overridden
    l = int(bank[0])
    r = -1

    # For each character in the battery bank
    for i in range(1, len(bank)):
        char = int(bank[i])

        # If it's the last character, set the 1s position to the max of its current value and the last character
        if i == len(bank) - 1:
            r = max(char, r)

        # If it's somewhere in the middle
        else:
            # If it's larger than the 10s digit, update the 10s digit and reset the right digit
            if char > l:
                l = char
                r = -1
            # Else, if it's larger than the 1s digit, update the 1s digit
            elif char > r:
                r = char

    return l * 10 + r


def find_max_overclocked_joltage(bank: str) -> int:

    # Select none of the digits except for the last 12
    selected = [(False if i < len(bank) - 12 else True) for i in range(len(bank))]

    # For each of the 12 batteries
    for i in range(12):
        last_selected = int(bank[-1])
        last_selected_index = -1

        # Loop through all digits
        for j in range(len(bank) - 1, -1, -1):
            current = int(bank[j])

            # If it's already selected, update selected pointers
            if selected[j]:
                last_selected = current
                last_selected_index = j

            # If it's not selected but the sum doesn't get worse by updating pointers, update
            elif current >= last_selected:
                last_selected = current
                selected[last_selected_index] = False

                last_selected_index = j
                selected[last_selected_index] = True

    # Collect selected digits and return as int
    return int("".join([bank[i] if selected[i] else "" for i in range(len(bank))]))


def solve_day_3_pt_1(battery_banks: list[str]) -> int:
    total_joltage = 0

    for bank in battery_banks:
        total_joltage += find_max_joltage(bank)

    return total_joltage


def solve_day_3_pt_2(battery_banks: list[str]) -> int:
    total_joltage = 0

    for bank in battery_banks:
        total_joltage += find_max_overclocked_joltage(bank)

    return total_joltage


if __name__ == "__main__":
    battery_banks = read_file("input.txt")

    print(solve_day_3_pt_1(battery_banks))
    print(solve_day_3_pt_2(battery_banks))
