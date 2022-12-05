#!/usr/bin/env python

import argparse
import sys
import os




parser = argparse.ArgumentParser(description="print list of directory contents")
parser.add_argument("-a", "--all", action='store_false', help="show hidden objects")
parser.add_argument("dir", help="path to directory", nargs='?', const="./", type=str)
args = parser.parse_args()

files = sorted(os.listdir(args.dir), key=str.lower)

if args.all:
    for file in files:
        if not file.startswith("."):
            sys.stdout.write(file + "\n")
else:
    sys.stdout.write(".\n..\n")
    for file in files:
        sys.stdout.write(file + "\n")


