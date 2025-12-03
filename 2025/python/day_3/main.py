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


def solve_day_3_pt_1(battery_banks: list[str]) -> int:
    total_joltage = 0

    for bank in battery_banks:
        total_joltage += find_max_joltage(bank)

    return total_joltage


if __name__ == "__main__":
    battery_banks = read_file("input.txt")

    print(solve_day_3_pt_1(battery_banks))
