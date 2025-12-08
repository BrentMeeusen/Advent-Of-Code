from helpers import read_file
import math


def d(a: tuple[int, ...], b: tuple[int, ...]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def merge(circuits: list[set]) -> list[set]:
    for i, circuit in enumerate(circuits):
        is_merged = False
        for j in range(i + 1, len(circuits)):
            if len(circuit.intersection(circuits[j])) > 0:
                circuit.update(circuits.pop(j))
                is_merged = True
                break

        # There is only one removal to be made, so we can stop the execution when this is done
        if is_merged:
            break

    return circuits


def generate_sorted_distances(coordinates: list[tuple[int, ...]]) -> list[tuple[int, int]]:
    return sorted({
        (i * len(coordinates) + j): (0 if j <= i else d(coordinate, coordinates[j]))
        for i, coordinate in enumerate(coordinates) for j in range(len(coordinates))
        if j > i
    }.items(), key=lambda item: item[1])


def solve_day_8_pt_1(coordinates: list[tuple[int, ...]], combinations: int) -> int:

    # Generate 1D distance "matrix" and sort from shortest to longest distances between two points
    sorted_distances = generate_sorted_distances(coordinates)

    # Loop over the smallest distances
    circuits: list[set] = []
    i = next(x for x, n in enumerate(sorted_distances) if n[1] > 0)

    for n in range(combinations):

        # Find the IDs of the coordinates that belong to the distance
        coordinate_id_1 = sorted_distances[i + n][0] // len(coordinates)
        coordinate_id_2 = sorted_distances[i + n][0] - (coordinate_id_1 * len(coordinates))
        curr_coordinates = {coordinate_id_1, coordinate_id_2}

        # If at least one of them is part of an existing circuit, extend circuit
        is_added = False
        for circuit in circuits:
            if len(circuit.intersection(curr_coordinates)) > 0:
                circuit.update(curr_coordinates)
                is_added = True
                break

        # If it wasn't added to an existing circuit, create a new one. Otherwise, merge sets where possible
        circuits = merge(circuits) if is_added else circuits + [{coordinate_id_1, coordinate_id_2}]

        if n % 100 == 99:
            print(f"Finished {n + 1} iterations")

    # Return the multiplication of the size of the three largest circuits
    return math.prod(sorted(map(len, circuits), reverse=True)[:3])


def solve_day_8_pt_2(coordinates: list[tuple[int, ...]]) -> int:

    # Generate 1D distance "matrix" and sort from shortest to longest distances between two points, create 1-element sets
    sorted_distances = generate_sorted_distances(coordinates)
    circuits = {n: {n} for n in range(len(coordinates))}

    # For each distance
    for coordinate_index, _ in sorted_distances:

        # Find the IDs of the coordinates that belong to the distance
        coordinate_id_1 = coordinate_index // len(coordinates)
        coordinate_id_2 = coordinate_index - (coordinate_id_1 * len(coordinates))

        # Merge circuits together and make sure each element of the element has the same set reference
        merged = circuits[coordinate_id_1] | circuits[coordinate_id_2]
        for coordinate_id in merged:
            circuits[coordinate_id] = merged

        # If the last merge made all circuits join into one big network, return
        if len(circuits[coordinate_id_2]) == len(coordinates):
            return coordinates[coordinate_id_1][0] * coordinates[coordinate_id_2][0]

    # Should not be reached
    return -1


if __name__ == "__main__":
    coordinates = read_file("input.txt")
    coordinates = list(map(lambda n: tuple(map(int, n.split(","))), coordinates))

    print(solve_day_8_pt_1(coordinates, 1000))
    print(solve_day_8_pt_2(coordinates))
