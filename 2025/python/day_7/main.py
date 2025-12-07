from helpers import read_file


def solve_day_7_pt_1(diagram: list[str]) -> int:
    beams = [diagram[0].find("S")]
    splitter_count = 0

    for row in diagram[1:]:
        next_beams = []

        for beam in beams:
            # If the beam encounters a splitter, increment count and create new beams
            if row[beam] == "^":
                splitter_count += 1
                next_beams.append(beam - 1)
                next_beams.append(beam + 1)

            # If we saw empty space, continue the beam
            else:
                next_beams.append(beam)

        # Remove duplicates and update beams for next row
        beams = list(set(next_beams))

    return splitter_count


def solve_day_7_pt_2(diagram: list[str]) -> int:
    possible_paths = [1 if diagram[0].find("S") == i else 0 for i in range(0, len(diagram[0]))]

    for row in diagram[1:]:
        next_beams = []

        for i, beam in enumerate(possible_paths):
            # If we've added an extra beam (because the previous one was a beam),
            # add the possible paths from the beam above, then skip this column
            if len(next_beams) > i:
                next_beams[-1] += beam
                continue
            # If there's no beam, there's no possible paths (yet)
            if beam == 0:
                next_beams.append(0)
            # If a beam touches a splitter, both the left and right path can be reached the same number
            # of times the current beam can be reached
            elif row[i] == "^":
                next_beams[-1] += beam
                next_beams.append(0)    # The row below the splitter cannot be reached
                next_beams.append(beam)
            # Else, just continue the beam
            else:
                next_beams.append(beam)

        # Update the possible paths
        possible_paths = next_beams

    return sum(possible_paths)


if __name__ == "__main__":
    diagram = read_file("input.txt")

    print(solve_day_7_pt_1(diagram))
    print(solve_day_7_pt_2(diagram))
