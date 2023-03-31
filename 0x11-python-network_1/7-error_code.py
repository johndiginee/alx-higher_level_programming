#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    urlName = sys.argv[1]

    requestData = requests.get(urlName)
    if requestData.status_code >= 400:
        print("Error code: {}".format(requestData.status_code))
    else:
        print(requestData.text)
