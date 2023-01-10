#!/usr/bin/python3
"""Module for writing a string to a text file"""


def write_file(filename="", text=""):
    """Method for readinng lines from file."""
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)
