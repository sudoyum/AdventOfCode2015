#!/usr/bin/env python3

import argparse
import re
import sys


def parse_input_line(line):
    m = re.match("(\d+)x(\d+)x(\d+)", line)
    if m:
        return int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        sys.exit(f"issue with regex parsing of line.. {line}")


def surface_area(l, w, h):
    lw = l * w
    wh = w * h
    hl = h * l
    return min(lw, wh, hl) + (2 * lw) + (2 * wh) + (2 * hl)


def min_perimeter(l, w, h):
    return min(2 * w + 2 * l, 2 * w + 2 * h, 2 * h + 2 * l)


def solve_p1(input_data):
    total = 0
    for line in input_data:
        length, width, height = parse_input_line(line)
        total += surface_area(length, width, height)
    print(f"PART1: {total}")


def solve_p2(input_data):
    total = 0
    for line in input_data:
        length, width, height = parse_input_line(line)
        bow = length * width * height
        total += bow + min_perimeter(length, width, height)
    print(f"PART2: {total}")


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
