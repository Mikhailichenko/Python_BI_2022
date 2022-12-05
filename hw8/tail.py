#!/usr/bin/env python

import argparse
import sys


def print_last_lines(path_to_file, lines):
    all_lines = path_to_file.readlines()
    n_lines = len(all_lines)
    last_lines = all_lines[n_lines - lines:]
    for line in last_lines:
        sys.stdout.write(line)


def print_from_line(path_to_file, lines):
    all_lines = path_to_file.readlines()
    last_lines = all_lines[lines-1:]
    for line in last_lines:
        sys.stdout.write(line)








parser = argparse.ArgumentParser(description="output the last part of files")
parser.add_argument('-n', '--lines',  nargs='?', type=str, const="10", default="10", help='output the last N lines, instead of the last  10; or  use  -n +N to output starting with line N')


if sys.stdin.isatty():
    parser.add_argument('path_to_file', help="path to file", nargs="+", type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
    path_to_file = parser.parse_args().path_to_file

else:
    parser.add_argument('--path_to_file', help="path to file", type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
    path_to_file = [parser.parse_args().path_to_file]


lines = parser.parse_args().lines


if lines[0] == "+":
    lines = int(lines[1:])
    for file in path_to_file:
        i = 1
        for line in file:
            if i < lines:
                i += 1
            else:
                sys.stdout.write(line)

else:
    lines = int(lines)
    for file in path_to_file:
        i = 0
        ans = []
        for line in file:
            if i < lines:
                ans.append(line)
                i += 1
            else:
                ans.append(line)
                ans.pop(0)
                
    for i in ans:
        sys.stdout.write(i)



