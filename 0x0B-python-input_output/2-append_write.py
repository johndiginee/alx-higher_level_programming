#!/usr/bin/python3
"""Module for appending string."""


def append_write(filename="", text=""):
    """Method for reading from file."""
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
