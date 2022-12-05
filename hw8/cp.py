#!/usr/bin/env python

import argparse
import sys
import os
import shutil



parser = argparse.ArgumentParser(description="copy files and directories")

parser.add_argument('-r', '--recursive', action='store_true', help='copy directories and their contents recursively')
parser.add_argument('path_to_input_file', help="path to input file", nargs='+', default=sys.stdin)
parser.add_argument('path_to_output_file', help="path to output file", type=str, default=sys.stdin)

args = parser.parse_args()
path_in_file = args.path_to_input_file
path_out_file = args.path_to_output_file

for input_file in path_in_file:
    if os.path.isfile(input_file):
        shutil.copy2(input_file, path_out_file)
    
    elif os.path.isdir(input_file):
        if args.recursive and os.path.exists(path_out_file):
            shutil.copytree(input_file, path_out_file+os.path.sep+os.path.basename(input_file))
        elif args.recursive and not os.path.exists(path_out_file):
            shutil.copytree(input_file, path_out_file)
        else:
            sys.stdout.write(f"cp: -r not specified; omitting directory '{input_file}'\n")

    else:
        sys.stdout.write("No such file or directory\n")




