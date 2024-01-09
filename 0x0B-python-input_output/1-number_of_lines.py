#!/usr/bin/python3
def number_of_lines(1-write_file.py=""):
    """ function that returns the number of lines of a text file """

    with open(1-write_file.py) as f:
        count = len(f.readlines())
    return count
