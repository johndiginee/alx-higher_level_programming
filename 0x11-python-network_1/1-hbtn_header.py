#!/usr/bin/python3
"""script that takes in a URL, sends a req"""
"""the value of the X-Request-Id variables."""
import urllib.request
import sys


if __name__ == "__main__":
    urlName = sys.argv[1]

    requestURL = urllib.request.Request(urlName)
    with urllib.request.urlopen(requestURL) as response:
        print(dict(response.headers).get("X-Request-Id"))
