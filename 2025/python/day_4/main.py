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


def remove_accessible_rolls(diagram: list[str]) -> list[str]:
    updated_diagram = [[cell for cell in row] for row in diagram]

    for x in range(len(diagram)):
        for y in range(len(diagram[x])):
            if has_less_than_four_neighbours(diagram, x, y):
                updated_diagram[x][y] = "."

    return updated_diagram


def solve_day_4_pt_1(diagram: list[str]) -> int:
    accessible_rolls = 0

    for i, row in enumerate(diagram):
        for j, cell in enumerate(row):
            if cell == "@" and has_less_than_four_neighbours(diagram, i, j):
                accessible_rolls += 1

    return accessible_rolls



def solve_day_4_pt_2(diagram: list[str]) -> int:
    total_accessible_rolls = 0
    currently_accessible_rolls = solve_day_4_pt_1(diagram)

    while currently_accessible_rolls > 0:
        total_accessible_rolls += currently_accessible_rolls
        diagram = remove_accessible_rolls(diagram)
        currently_accessible_rolls = solve_day_4_pt_1(diagram)

    return total_accessible_rolls


if __name__ == "__main__":
    diagram = read_file("input.txt")

    print(solve_day_4_pt_1(diagram))
    print(solve_day_4_pt_2(diagram))
