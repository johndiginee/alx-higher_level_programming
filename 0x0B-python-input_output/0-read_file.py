#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Method for reading from file."""
    with open(filename, "r", encoding="utf-8") as myFile:
        text = myFile.read()
	print(text, end="")
