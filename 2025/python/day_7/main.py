from helpers import read_file
import re
import math


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
    pass


if __name__ == "__main__":
    diagram = read_file("input.txt")

    print(solve_day_7_pt_1(diagram))
    # print(solve_day_7_pt_2(diagram))
