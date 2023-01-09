#!/usr/bin/python3
"""A class for lookup method."""


def lookup(obj):
    """Looks up object attributes and methods.
    Args:
        obj (object): the object to list.
    Returns:
        list: the list of attributes.
    """
    return dir(obj)