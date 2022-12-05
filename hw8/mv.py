#!/usr/bin/env python

import sys
import argparse
import shutil


parser = argparse.ArgumentParser(description="move (rename) files")
parser.add_argument('path_to_input_file', help="path to input file", nargs='+', default=sys.stdin)
parser.add_argument('path_to_output_file', help="path to dir where files should be moved", type=str, default=sys.stdin)


for input_file in parser.parse_args().path_to_input_file:
    shutil.move(input_file, parser.parse_args().path_to_output_file)

