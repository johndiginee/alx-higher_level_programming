#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    urlName = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(urlName.text)))
    print("\t- content: {}".format(urlName.text))
