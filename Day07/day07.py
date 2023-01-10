#!/usr/bin/env python3

import argparse
import copy
import re
import sys


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Inst:
    def __init__(self, op, dst, src1, src2=None, shift=None):
        self.op = op
        self.dst = dst
        self.src1 = src1
        self.src2 = src2
        self.shift = shift

    def ready(self, resolved):
        if self.dst in resolved:
            return False
        if self.src1 not in resolved and not is_number(self.src1):
            return False
        if self.src2:
            if self.src2 not in resolved:
                return False
        return True

    def run(self, resolved):
        if self.op == "DIR":
            return resolved[self.src1]
        elif self.op == "NOT":
            return ~resolved[self.src1] & 0xFFFF
        elif self.op == "AND":
            if is_number(self.src1):
                return int(self.src1) & resolved[self.src2]
            else:
                return resolved[self.src1] & resolved[self.src2]
        elif self.op == "OR":
            return resolved[self.src1] | resolved[self.src2]
        elif self.op == "LSHIFT":
            return resolved[self.src1] << self.shift
        elif self.op == "RSHIFT":
            return resolved[self.src1] >> self.shift


def parse_input(input_data):
    instructions = []
    resolved = {}

    for line in input_data:
        assign_match = re.match("(\d+) -> (\w+)", line)
        direct_match = re.match("(\w+) -> (\w+)", line)
        logic_match = re.match(
            "(?P<src1>\w+) (?P<inst>AND|OR|RSHIFT|LSHIFT) (?P<src2>\w+) -> (?P<dest>\w+)",
            line,
        )
        not_match = re.match("NOT (\w+) -> (\w+)", line)

        if assign_match:
            resolved[assign_match.group(2)] = int(assign_match.group(1))

        if direct_match:
            instructions.append(
                Inst("DIR", direct_match.group(2), direct_match.group(1), None)
            )

        if logic_match:
            src1, op, src2, dst = logic_match.groups()
            if op == "RSHIFT" or op == "LSHIFT":
                instructions.append(Inst(op, dst, src1, None, int(src2)))
            else:
                instructions.append(Inst(op, dst, src1, src2))
        if not_match:
            instructions.append(
                Inst("NOT", not_match.group(2), not_match.group(1), None)
            )
    return (instructions, resolved, len(input_data))


def run_instructions(instructions, resolved, num_total):
    while len(resolved) != num_total:
        for inst in instructions:
            if inst.ready(resolved):
                resolved[inst.dst] = inst.run(resolved)
    return resolved["a"]


def solve_p1(parsed_data):
    instructions, resolved, num_total = copy.deepcopy(parsed_data)
    print(f"PART1: {run_instructions(instructions, resolved, num_total)}")


def solve_p2(parsed_data):
    instructions, resolved, num_total = parsed_data
    resolved["b"] = 956
    print(f"PART2: {run_instructions(instructions, resolved, num_total)}")


def run_solutions(input_file, part):
    with open(input_file, "r") as file_handle:
        input_data = file_handle.read().splitlines()

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
