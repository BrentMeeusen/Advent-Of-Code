from helpers import read_file


def solve_day_5_pt_1(ranges: list[range], ids: list[int]) -> int:
    fresh_id_count = 0

    for id in ids:
        for range in ranges:
            if id in range:
                fresh_id_count += 1
                break

    return fresh_id_count


def solve_day_5_pt_2(inputs: list[str]) -> int:
    possible_fresh_id_count = 0

    # Get all ranges from input
    ranges = []
    for row in inputs:
        if row == "":
            break

        # Get min-max for current range
        r_min, r_max = tuple(map(int, row.split("-")))

        # Update min-max to only apply to IDs that aren't in a range already to prevent counting IDs multiple times,
        # and exclude fully submerged ranges
        excluded = 0
        for range in ranges:
            # If r_min partially overlaps range, exclude overlap
            if range[0] <= r_min <= range[1]:
                r_min = range[1] + 1

            # If r_max partially overlaps range, exclude overlap
            if range[0] <= r_max <= range[1]:
                r_max = range[0] - 1

            # If our (updated) range fully submerges the smaller range, exclude the smaller range
            if r_min <= range[0] and r_max >= range[1]:
                excluded += range[1] - range[0] + 1

        # If there's at least one value to add, add it
        if r_min <= r_max:
            possible_fresh_id_count += r_max - r_min + 1
            ranges.append((r_min, r_max))

        # Remove fully submerged counts
        possible_fresh_id_count -= excluded

    return possible_fresh_id_count


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
    print(solve_day_5_pt_2(inputs))
