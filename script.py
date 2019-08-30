#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 3:
    sys.exit(f"Please input a file and string to search!\nUsage: {sys.argv[0]} \"[string to search]\" [files (whitespace separated)]")

try:
    for file_name in sys.argv[2:]:
        with open(file_name) as file:
            for i, line in enumerate(file):
                if sys.argv[1] in line:
                    print(f"[{file_name}] Line {i + 1}: {line}")
except:
    sys.exit(f"Error trying to open {sys.argv[1]}")
