#!/usr/bin/python3
"""A class for MyInt class."""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, other):
        """Override equals, inverting it."""
        return self.real != other

    def __ne__(self, other):
        """Override not-equals, inverting it."""
        return self.real == other
