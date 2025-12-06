from helpers import read_file
import re
import math


def parse_numbers(numbers_lists: list[str]) -> list[list[int]]:
    return [list(map(int, re.split(r"\s+", numbers_list.strip()))) for numbers_list in numbers_lists]


def parse_operators(operators: str) -> list[str]:
    return re.split(r"\s+", operators.strip())


def solve_day_6_pt_1(numbers_lists: list[list[int]], operators: list[str]) -> int:
    total_sum = 0

    # Define addition and multiplication functions
    addition = lambda ns: sum(ns)
    multiplication = lambda ns: math.prod(ns)

    # For each number, select mathematical operation and perform operation on all items
    for i in range(len(numbers_lists[0])):
        f = addition if operators[i] == "+" else multiplication
        numbers = [n[i] for n in numbers_lists]

        total_sum += f(numbers)

    return total_sum


def solve_day_6_pt_2(inputs: list[str]) -> int:
    pass


if __name__ == "__main__":
    inputs = read_file("input.txt")
    numbers = parse_numbers(inputs[:-1])
    operators = parse_operators(inputs[-1])

    print(solve_day_6_pt_1(numbers, operators))
    # print(solve_day_6_pt_2(numbers, operators))
