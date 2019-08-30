#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 3:
    sys.exit(f"Please input a file and string to search!\nUsage: {sys.argv[0]} [file to search in] [string to search]")

try:
    query = " ".join(sys.argv[2:])

    with open(sys.argv[1]) as file:
        for i, line in enumerate(file):
            if query in line:
                print(f"Line {i + 1}: {line}")
except:
    sys.exit(f"Error trying to open {sys.argv[1]}")
