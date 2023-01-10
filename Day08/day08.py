#!/usr/bin/env python3

import argparse


class UnexpectedInputError(Exception):
    pass


def num_parsed_chars(input_str):
    if input_str[0] == '"' and input_str[-1] == '"':
        input_str = input_str[1:-1]
    else:
        raise UnexpectedInputError("Input string doesn't started and end with '\"'")

    count = len(input_str)
    index = 0

    while index < len(input_str[:-1]):
        if input_str[index] == "\\":
            if input_str[index + 1] == "x":
                index += 4
                count -= 3
            elif input_str[index + 1] == '"' or input_str[index + 1] == "\\":
                index += 2
                count -= 1
        else:
            index += 1

    return count


def num_expanded_chars(input_str):
    count = len(input_str)
    index = 0

    while index < len(input_str):
        if input_str[index] == "\\":
            # Special case for last character in string
            if input_str[index + 1] != '"' or index + 1 == len(input_str) - 1:
                count += 1
        elif input_str[index] == '"':
            count += 2
        index += 1

    return count


def solve_p1(input_data):
    total_chars, memory_chars = 0, 0
    for input_str in input_data:
        total_chars += len(input_str)
        memory_chars += num_parsed_chars(input_str)

    print(f"PART1: {total_chars - memory_chars}")


def solve_p2(input_data):
    total_chars, memory_chars = 0, 0
    for input_str in input_data:
        total_chars += len(input_str)
        memory_chars += num_expanded_chars(input_str)

    print(f"PART2: {memory_chars - total_chars}")


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
    except UnexpectedInputError as uie_exception:
        print(f"Input data not in expected format: {uie_exception}")


if __name__ == "__main__":
    main()
