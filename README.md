# PyGrep
A simple reimplementation of "grep" made in Python

## How to use
Just run the the file script.py if you want it as a CLI tool (Usage: `script.py "string to search" file1 file2`. You don't need to specify multiple files.)

If you want it as a function to use in your own project import the lib.py file and use it as follows:
```py
import lib

lib.grep("Test", ["file1", "file2"])
```
