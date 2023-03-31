#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    urlName = sys.argv[1]

    requestURL = requests.get(urlName)
    print(requestURL.headers.get("X-Request-Id"))
