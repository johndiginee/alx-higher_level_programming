#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        bodyResponse = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(bodyResponse)))
        print("\t- content: {}".format(bodyResponse))
        print("\t- utf8 content: {}".format(bodyResponse.decode("utf-8")))
