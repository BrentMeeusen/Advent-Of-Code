from helpers import read_file
import re
import math


def parse_numbers(numbers_lists: list[str]) -> list[list[str]]:
    return [re.split(r"\s+", numbers_list.strip()) for numbers_list in numbers_lists]


def parse_operators(operators: str) -> list[str]:
    return re.split(r"\s+", operators.strip())


def addition(ns):
    return sum(ns)

def multiplication(ns):
    return math.prod(ns)


def solve_day_6_pt_1(numbers_lists: list[list[str]], operators: list[str]) -> int:
    total_sum = 0
    numbers_lists = [list(map(int, numbers_list)) for numbers_list in numbers_lists]

    # For each number, select mathematical operation and perform operation on all items
    for i in range(len(numbers_lists[0])):
        f = addition if operators[i] == "+" else multiplication
        numbers = [n[i] for n in numbers_lists]

        total_sum += f(numbers)

    return total_sum


def solve_day_6_pt_2(inputs: list[str], numbers_lists: list[list[str]], operators: list[str]) -> int:

    # Split numbers to needed lengths and replace whitespaces with 0s
    whitespace_numbers_lists = []
    j = 0
    for i in range(len(numbers_lists[0])):
        longest_str_len = len(max([numbers_list[i] for numbers_list in numbers_lists], key=len))
        whitespace_numbers_lists.append([ns[j:j + longest_str_len] for ns in inputs])
        j += longest_str_len + 1

    # Reform numbers
    reformed_numbers = []
    for whitespace_numbers_list in whitespace_numbers_lists:
        reformed_numbers.append([
            int("".join([whitespace_numbers_list[i][j] for i in range(len(whitespace_numbers_list))]))
            for j in range(len(whitespace_numbers_list[0]))
        ])

    # Solve
    total_sum = 0
    for i, numbers in enumerate(reformed_numbers):
        f = addition if operators[i] == "+" else multiplication
        total_sum += f(numbers)

    return total_sum


if __name__ == "__main__":
    inputs = read_file("input.txt")
    numbers = parse_numbers(inputs[:-1])
    operators = parse_operators(inputs[-1])

    print(solve_day_6_pt_1(numbers, operators))
    print(solve_day_6_pt_2(inputs[:-1], numbers, operators))
