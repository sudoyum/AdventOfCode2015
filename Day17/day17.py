#!/usr/bin/env python3

import argparse
import itertools


def solve_p1(containers):
    exact_fit = 0
    for i in range(len(containers)):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == 150:
                exact_fit += 1
    print(f"PART1: {exact_fit}")


def solve_p2(containers):
    occurrences = [0] * len(containers)
    for i in range(len(containers)):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == 150:
                occurrences[len(combination)] += 1
    min_containers = next((i for i in occurrences if i != 0))
    print(f"PART2: {min_containers}")


def parse_input(input_data):
    containers = []
    for line in input_data:
        containers.append(int(line.strip("\n")))
    return containers


def run_solutions(input_file, part):
    with open(input_file, "r", encoding="utf-8") as file_handle:
        input_data = file_handle.read().splitlines()

    containers = parse_input(input_data)

    if part == "p1":
        solve_p1(containers)
    elif part == "p2":
        solve_p2(containers)
    elif part == "both":
        solve_p1(containers)
        solve_p2(containers)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file containing puzzle input", type=str)
    parser.add_argument("part", help="", type=str, choices=["p1", "p2", "both"])

    args = parser.parse_args()

    try:
        run_solutions(args.input_file, args.part)
    except IOError as io_exception:
        print(f"Opening file error: {io_exception.strerror} - {args.input_file}")


if __name__ == "__main__":
    main()
