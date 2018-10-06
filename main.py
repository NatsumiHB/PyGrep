import sys
import os

if len(sys.argv) < 3:
    print("Please input a file and string to search!")
    print("Usage: python3 main.py [file to search in] [string to search]")
    sys.exit()

if not os.path.isfile(sys.argv[1]):
    print("That file doesn't exist")
    sys.exit()

file = open(sys.argv[1])
query = " ".join(sys.argv[2:])

for line in file:
    if query in line:
        print(line)