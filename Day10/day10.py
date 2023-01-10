#!/usr/bin/env python3

import argparse


def exp_seq(buf):
    return str(len(buf)) + buf[0]


def expand(seq):
    state = 0
    expanded_seq = ""
    buf = ""
    for i, c in enumerate(seq):
        if len(buf) == 0 or buf[-1] == c:
            buf += c
        else:
            if buf[-1] != c:
                expanded_seq += exp_seq(buf)
            buf = c

        if i + 1 == len(seq):
            # last char
            expanded_seq += exp_seq(buf)
    return expanded_seq


def solve_p1(input_data):
    res = expand(input_data[0])
    for i in range(0, 39):
        res = expand(res)
    print(f"PART1: {len(res)}")


def solve_p2(input_data):
    res = expand(input_data[0])
    for i in range(0, 49):
        res = expand(res)
    print(f"PART2: {len(res)}")


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file containing puzzle input", type=str)
    parser.add_argument("part", help="", type=str, choices=["p1", "p2", "both"])

    args = parser.parse_args()

    run_solutions(args.input_file, args.part)
