from helpers import read_file


def solve_day_5_pt_1(ranges: list[range], ids: list[int]) -> int:
    fresh_id_count = 0

    for id in ids:
        for range in ranges:
            if id in range:
                fresh_id_count += 1
                break

    return fresh_id_count


def split_inputs(inputs: list[str]) -> tuple[list[range], list[int]]:
    ranges = []
    ids = []

    is_range = True
    for row in inputs:
        if row == "":
            is_range = False

        elif is_range:
            r_min, r_max = row.split("-")
            ranges.append(range(int(r_min), int(r_max) + 1))
        else:
            ids.append(int(row))

    return ranges, ids


if __name__ == "__main__":
    inputs = read_file("input.txt")
    ranges, ids = split_inputs(inputs)

    print(solve_day_5_pt_1(ranges, ids))
    # print(solve_day_5_pt_2(diagram))
