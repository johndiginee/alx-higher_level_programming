#!/usr/bin/python3
"""Medule for load_from_json_file method"""
import json


def load_from_json_file(filename):
    """Method for loading from json file."""
    with open(filename, "r", encoding="utf-8") as myFile:
        return json.load(myFile)
