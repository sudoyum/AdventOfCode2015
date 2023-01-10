#!/usr/bin/env python3

import argparse
import hashlib


def hash_iterations(input_data, starting_digits):
    iterations = 0
    while True:
        input_str = input_data[0] + str(iterations)
        md5_hash = hashlib.md5(input_str.encode())
        if md5_hash.hexdigest()[:starting_digits] == "0" * starting_digits:
            break
        iterations += 1
    return iterations


def solve_p1(input_data):
    print(f"PART1: {hash_iterations(input_data, 5)}")


def solve_p2(input_data):
    print(f"PART2: {hash_iterations(input_data, 6)}")


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
