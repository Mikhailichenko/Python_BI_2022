#!/usr/bin/env python

import argparse
import sys
import os





parser = argparse.ArgumentParser(description="make links")
parser.add_argument('-s', '--symbolic', action='store_true', help="make symbolic links instead of hard links")

parser.add_argument('path_to_input_file', help="path to input file", type=str, default=sys.stdin)
parser.add_argument('new_link', help="new link", type=str, default=sys.stdin) 


         
if parser.parse_args().symbolic:
    os.symlink(parser.parse_args().path_to_input_file, parser.parse_args().new_link)
else:
    os.link(parser.parse_args().path_to_input_file, parser.parse_args().new_link)











         
