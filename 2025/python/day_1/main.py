from helpers import read_file


def parse_instruction(instruction: str) -> int:
    """
    Parse the instruction string.
    :param instruction: The instruction string.
    :return: How far the knob should be turned.
    """
    return int(instruction[1:]) * (1 if instruction[0] == "R" else -1)


def solve_day_1(instructions: list[str]) -> int:
    current_pos = 50
    zero_count = 0

    for instruction in instructions:
        current_pos = (current_pos + parse_instruction(instruction)) % 100

        if current_pos == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    print(solve_day_1(read_file("input.txt")))
