#!/usr/bin/env python3

import argparse
import json
import re


def total_ints(j, total):
    local_total = total
    for i in j:
        if isinstance(i, int):
            local_total += i
        elif isinstance(i, dict):
            if "red" not in i.values():
                local_total += total_ints(list(i.values()), total)
        elif isinstance(i, list):
            local_total += total_ints(i, total)
    return local_total


def solve_p1(input_data):
    matches = re.findall("[-0-9]+", input_data[0])
    total = sum([int(m) for m in matches])
    print(f"PART1: {total}")


def solve_p2(input_data):
    json_data = json.loads(input_data[0])
    t = total_ints(json_data.values(), 0)
    print(f"PART2: {t}")


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
