from helpers import read_file


def has_less_than_four_neighbours(diagram: list[str], x: int, y: int) -> bool:
    x_range = [x_pos for x_pos in range(x - 1, x + 2) if 0 <= x_pos < len(diagram)]
    y_range = [y_pos for y_pos in range(y - 1, y + 2) if 0 <= y_pos < len(diagram[0])]

    neighbours = -1     # -1 to compensate for the cell we're investigating
    for x in x_range:
        for y in y_range:
            if diagram[x][y] == "@":
                neighbours += 1

    return neighbours < 4


def solve_day_4_pt_1(diagram: list[str]) -> int:
    accessible_rolls = 0

    for i, row in enumerate(diagram):
        for j, cell in enumerate(row):
            if cell == "@" and has_less_than_four_neighbours(diagram, i, j):
                accessible_rolls += 1

    return accessible_rolls



def solve_day_4_pt_2(paper_roll_diagram: list[str]) -> int:
    pass


if __name__ == "__main__":
    diagram = read_file("input.txt")

    print(solve_day_4_pt_1(diagram))
    # print(solve_day_4_pt_2(diagram))
