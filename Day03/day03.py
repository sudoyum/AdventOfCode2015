#!/usr/bin/env python3

import argparse


def solve_p1(input_data):
    pos_x, pos_y = 0, 0
    houses = set()
    for char in input_data[0]:
        if char == "^":
            pos_y += 1
        elif char == "v":
            pos_y -= 1
        elif char == ">":
            pos_x += 1
        elif char == "<":
            pos_x -= 1
        houses.add((pos_x, pos_y))
    print(f"PART1: {len(houses)}")


def solve_p2(input_data):
    pos_x, pos_y = 0, 0
    rpos_x, rpos_y = 0, 0
    houses = set()
    for index, char in enumerate(input_data[0]):
        if index % 2 == 0:
            if char == "^":
                pos_y += 1
            elif char == "v":
                pos_y -= 1
            elif char == ">":
                pos_x += 1
            elif char == "<":
                pos_x -= 1
            houses.add((pos_x, pos_y))
        else:
            if char == "^":
                rpos_y += 1
            elif char == "v":
                rpos_y -= 1
            elif char == ">":
                rpos_x += 1
            elif char == "<":
                rpos_x -= 1
            houses.add((rpos_x, rpos_y))
    print(f"PART2: {len(houses)}")


def run_solutions(input_file, part):
    with open(input_file, "r", encoding="utf-8") as file_handle:
        input_data = file_handle.read().splitlines()

    if part == "p1":
        solve_p1(input_data)
    elif part == "p2":
        solve_p2(input_data)
    elif part == "both":
        solve_p1(input_data)
        solve_p2(input_data)


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
