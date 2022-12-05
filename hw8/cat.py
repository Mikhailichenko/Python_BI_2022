#!/usr/bin/env python

import argparse
import sys

    
parser = argparse.ArgumentParser(description="concatenate files and print on the standard output")
parser.add_argument('path_to_files', help="path to files", nargs="+", default=sys.stdin)

path=parser.parse_args().path_to_files

for file in path:
    with open(file) as f:
        for line in f:
            sys.stdout.write(line)
