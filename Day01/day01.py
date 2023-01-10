#!/usr/bin/env python3

import argparse


def solve_p1(input_data):
    floor = input_data[0].count("(") - input_data[0].count(")")
    print(f"PART1: {floor}")


def solve_p2(input_data):
    floor, index = 0, 0

    # solution index starts at 1
    for index, character in enumerate(input_data[0], start=1):
        floor += 1 if character == "(" else -1
        if floor < 0:
            break
    print(f"PART2: {index}")


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
