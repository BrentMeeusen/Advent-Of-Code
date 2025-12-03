from helpers import read_file


def parse_inputs_to_ranges(inputs: str) -> list[range]:
    ranges = []

    for r in inputs.split(","):
        dash_index = r.find("-")
        ranges.append(range(int(r[:dash_index]), int(r[dash_index + 1:]) + 1))

    return ranges


def has_repeating_patterns(s: str) -> bool:
    if len(s) % 2 == 1:
        return False

    return s[:int(len(s) / 2)] == s[int(len(s) / 2):]


def solve_day_2_pt_1(ranges: list[range]) -> int:
    invalid_ids = []

    for r in ranges:
        for n in r:
            if has_repeating_patterns(str(n)):
                invalid_ids.append(n)

    return sum(invalid_ids)


if __name__ == "__main__":
    problem_input = read_file("input.txt")[0]
    problem_ranges = parse_inputs_to_ranges(problem_input)

    print(solve_day_2_pt_1(problem_ranges))
