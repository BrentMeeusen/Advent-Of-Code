from helpers import read_file


def parse_instruction(instruction: str) -> int:
    """
    Parse the instruction string.
    :param instruction: The instruction string.
    :return: How far the knob should be turned.
    """
    return int(instruction[1:]) * (1 if instruction[0] == "R" else -1)


def solve_day_1_pt_1(instructions: list[str]) -> int:
    current_pos = 50
    zero_count = 0

    for instruction in instructions:
        current_pos = (current_pos + parse_instruction(instruction)) % 100

        if current_pos == 0:
            zero_count += 1

    return zero_count


def solve_day_1_pt_2(instructions: list[str]) -> int:
    current_pos = 50
    zero_count = 0

    for instruction in instructions:
        num_clicks = parse_instruction(instruction)
        direction = 1 if num_clicks > 0 else -1

        while abs(num_clicks) > 0:
            current_pos = (current_pos + direction) % 100
            num_clicks -= direction

            if current_pos == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    instructions = read_file("input.txt")

    print(solve_day_1_pt_1(instructions))
    print(solve_day_1_pt_2(instructions))
