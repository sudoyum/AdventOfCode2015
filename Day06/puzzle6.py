#!/usr/bin/env python3

import argparse
import re
import sys


class Plane:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._plane = [[0 for x in range(rows)] for y in range(cols)]

    def print(self):
        for j in range(self._cols - 1, -1, -1):
            for i in range(0, self._rows):
                sys.stdout.write(f"{self._plane[i][j]} ")
            sys.stdout.write("\n")

    def set_range(self, low_x, high_x, low_y, high_y, val, toggle=False):
        for i in range(low_x, high_x + 1):
            for j in range(low_y, high_y + 1):
                if toggle:
                    self._plane[i][j] ^= 1
                else:
                    self._plane[i][j] = val

    def set_range_p2(self, low_x, high_x, low_y, high_y, val, toggle=False):
        for i in range(low_x, high_x + 1):
            for j in range(low_y, high_y + 1):
                if toggle:
                    self._plane[i][j] += 2
                else:
                    if val:
                        self._plane[i][j] += 1
                    else:
                        if self._plane[i][j] > 0:
                            self._plane[i][j] -= 1

    def count_on(self):
        count = 0
        for i in range(0, self._rows):
            for j in range(0, self._cols):
                if self._plane[i][j]:
                    count += self._plane[i][j]
        return count


def solve_p1(input_data):
    p = Plane(1000, 1000)
    num_lights = 0
    for instruction in input_data:
        match = re.search(
            r"(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)", instruction
        )
        if match:
            low_x, low_y = match.group(2).split(",")
            high_x, high_y = match.group(3).split(",")
            if match.group(1) == "turn on":
                p.set_range(int(low_x), int(high_x), int(low_y), int(high_y), 1)
            elif match.group(1) == "turn off":
                p.set_range(int(low_x), int(high_x), int(low_y), int(high_y), 0)
            else:
                p.set_range(
                    int(low_x), int(high_x), int(low_y), int(high_y), 0, toggle=True
                )

    print(f"PART1: {p.count_on()}")


def solve_p2(input_data):
    p = Plane(1000, 1000)
    num_lights = 0
    for instruction in input_data:
        match = re.search(
            r"(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)", instruction
        )
        if match:
            low_x, low_y = match.group(2).split(",")
            high_x, high_y = match.group(3).split(",")
            if match.group(1) == "turn on":
                p.set_range_p2(int(low_x), int(high_x), int(low_y), int(high_y), 1)
            elif match.group(1) == "turn off":
                p.set_range_p2(int(low_x), int(high_x), int(low_y), int(high_y), 0)
            else:
                p.set_range_p2(
                    int(low_x), int(high_x), int(low_y), int(high_y), 0, toggle=True
                )

    print(f"PART2: {p.count_on()}")


def run_solutions(input_file, part):
    with open(input_file, "r") as file_handle:
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
