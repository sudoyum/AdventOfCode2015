#!/usr/bin/env python3

import argparse
import re
from itertools import permutations


class UnexpectedInputError(Exception):
    pass


def calc_path_len(path, distances):
    path_len = 0

    start = path.pop()
    while path:
        dest = path.pop()
        try:
            path_len += distances[start, dest]
        except KeyError:
            path_len += distances[dest, start]
        start = dest
    return path_len


def solve_p1(parsed_data):
    cities = set()
    for city_pair in parsed_data.keys():
        start, dest = city_pair
        cities.add(start)
        cities.add(dest)

    shortest_path = None
    for path in list(permutations(cities)):
        path_len = calc_path_len(list(path), parsed_data)
        if shortest_path is None or path_len < shortest_path:
            shortest_path = path_len

    print(f"PART1: {shortest_path}")


def solve_p2(parsed_data):
    cities = set()
    for city_pair in parsed_data.keys():
        start, dest = city_pair
        cities.add(start)
        cities.add(dest)

    longest_path = None
    for path in list(permutations(cities)):
        path_len = calc_path_len(list(path), parsed_data)
        if longest_path is None or path_len > longest_path:
            longest_path = path_len

    print(f"PART2: {longest_path}")


def parse_input(input_data):
    parsed_data = {}
    for line in input_data.splitlines():
        regex_matches = re.search(r"(\w+) to (\w+) = (\d+)", line)
        if regex_matches:
            start, dest, dist = regex_matches.groups()
            parsed_data[start, dest] = int(dist)
        else:
            raise UnexpectedInputError(f"Issue with regex for input {line}")

    return parsed_data


def run_solutions(input_file, part):
    with open(input_file, "r") as file_handle:
        input_data = file_handle.read()

    parsed_data = parse_input(input_data)

    if part == "p1":
        solve_p1(parsed_data)
    elif part == "p2":
        solve_p2(parsed_data)
    elif part == "both":
        solve_p1(parsed_data)
        solve_p2(parsed_data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file containing puzzle input", type=str)
    parser.add_argument("part", help="", type=str, choices=["p1", "p2", "both"])

    args = parser.parse_args()

    try:
        run_solutions(args.input_file, args.part)
    except IOError as io_exception:
        print(f"Opening file error: {io_exception.strerror} - {args.input_file}")
    except UnexpectedInputError as uie_exception:
        print(f"Input data not in expected format: {uie_exception}, exiting")


if __name__ == "__main__":
    main()
