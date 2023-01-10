#!/usr/bin/env python3

import argparse


def banned_chars(password):
    return any(char in password for char in "iol")


def three_consecutive(password):
    for i in range(len(password) - 2):
        seq = password[i : i + 3]
        if (ord(seq[0]) + 1 == ord(seq[1])) and (ord(seq[1]) + 1 == ord(seq[2])):
            return True
    return False


def two_pairs(password):
    i = 0
    found = 0
    while True:
        if i + 1 >= len(password):
            return found == 2
        if password[i] == password[i + 1]:
            found += 1
            i += 2
        else:
            i += 1


def inc_password(password):
    new_password = []
    carry = True
    i = -1
    while carry:
        carry = password[i] == "z"
        if not carry:
            new_char = chr(ord(password[i]) + 1)
            if banned_chars(new_char):
                new_char = chr(ord(new_char) + 1)
            new_password.insert(0, new_char)
        else:
            new_password.insert(0, "a")
            i -= 1
    return password[0 : len(password) - len(new_password)] + "".join(new_password)


def next_password(password):
    first = True
    while True:
        if (
            banned_chars(password)
            or not three_consecutive(password)
            or not two_pairs(password)
            or first
        ):
            password = inc_password(password)
            first = False
        else:
            break
    return password


def solve_p1(input_data):
    print(f"PART1: {next_password(input_data)}")


def solve_p2(input_data):
    print(f"PART2: {next_password(next_password(input_data))}")


def run_solutions(input_file, part):
    with open(input_file, "r", encoding="utf-8") as file_handle:
        input_data = file_handle.read().splitlines()[0]

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
