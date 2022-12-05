#!/usr/bin/env python

import argparse
import sys


def count_lines(txt):
    return txt.count("\n")


def count_words(txt):
    w_count = 0
    for word in txt.split():
        w_count += 1
    
    return w_count


def count_bytes(txt):
    return len(txt.encode('utf-8'))


def output(txt, funcs):
    if all(funcs.values()):
        for func in funcs.keys():
            sys.stdout.write(str(func(txt)) + "\t")
    else:
        for func, value in funcs.items():
            if not value:
                sys.stdout.write(str(func(txt)) + "\t")



parser = argparse.ArgumentParser(description="Count newline, word, and byte for a file")

parser.add_argument('-l', '--lines', action='store_false', help='print number of newline')
parser.add_argument('-w', '--words', action='store_false', help='print number of bytes words')
parser.add_argument('-c', '--bytes', action='store_false', help='print number of bytes')




if sys.stdin.isatty():
    parser.add_argument('path_to_file', help="path to file",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
else:
    parser.add_argument('--path_to_file', help="path to file", default=sys.stdin)


args = parser.parse_args()
file = args.path_to_file.read()
funcs = {count_lines: args.lines, count_words: args.words, count_bytes: args.bytes}
output(file, funcs)
sys.stdout.write("\n")





