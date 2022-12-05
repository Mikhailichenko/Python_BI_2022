#!/usr/bin/env python

import argparse
import sys

def sort(path_to_file):
    all_lines = [line for file in path_to_file for line in file]
    sd_ls = sorted(all_lines, key=lambda x: re.sub('[^A-Za-z0-9]*', '', x).lower())
    for ls in sd_ls:
        sys.stdout.write(ls)
    return



    if sys.stdin.isatty():
        parser.add_argument('path_to_file', help="path to file", nargs="+",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        sort_alphabetical(path_to_file=args.path_to_file)
    else:
        parser.add_argument('--path_to_file', help="path to file",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        sort_alphabetical(path_to_file=[args.path_to_file])
        
        

parser = argparse.ArgumentParser(description="Sort lines of text files in alphabetical order")

if sys.stdin.isatty():
    parser.add_argument('path_to_file', help="path to file", nargs="+", type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
    path_to_file = parser.parse_args().path_to_file

else:
    parser.add_argument('--path_to_file', help="path to file", type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
    path_to_file = [parser.parse_args().path_to_file]


lines = [line for file in path_to_file for line in file]

sorted_lines = sorted(lines, key=lambda x: x.lower())
for line in sorted_lines:
    sys.stdout.write(line)







