#!/usr/bin/env python

import argparse
import sys
import os
import shutil


parser = argparse.ArgumentParser(description="remove a file or directory")
parser.add_argument('-r', '--recursive', action='store_true', help='recursively remove directories and their contents')
parser.add_argument('path_to_file', help="path to file", type=str, default=sys.stdin)



path = parser.parse_args().path_to_file


if os.path.isfile(path):
    os.remove(path)
elif os.path.isdir(path):
    if parser.parse_args().recursive:
        shutil.rmtree(path)
    else:
        os.rmdir(path)
else:
    sys.stdout.write("No such file or directory\n")
