#!/usr/bin/env python3

import argparse
from collections import Counter


def is_banned_string(entry):
    return "ab" in entry or "cd" in entry or "pq" in entry or "xy" in entry


def double_letter(entry):
    for index in range(0, len(entry) - 1):
        if entry[index] == entry[index + 1]:
            return True
    return False


def three_vowels(entry):
    counter = Counter(entry)
    count = 0
    for vowel in "aeiou":
        count += counter[vowel]
    return count >= 3


def solve_p1(parsed_data):
    nice_count = 0
    for entry in parsed_data:
        if not is_banned_string(entry) and double_letter(entry) and three_vowels(entry):
            nice_count += 1
    print(f"PART1: {nice_count}")


def repeat_between(entry):
    for index in range(0, len(entry) - 2):
        if entry[index] == entry[index + 2]:
            return True
    return False


def double_nooverlap(entry):
    for index in range(0, len(entry)):
        for i in range(index + 2, len(entry) - 1):
            if entry[index : index + 2] == entry[i : i + 2]:
                return True
    return False


def solve_p2(parsed_data):
    nice_count = 0
    for entry in parsed_data:
        if double_nooverlap(entry) and repeat_between(entry):
            nice_count += 1
    print(f"PART2: {nice_count}")


def parse_input(input_data):
    parsed_data = input_data.splitlines()
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


if __name__ == "__main__":
    main()
