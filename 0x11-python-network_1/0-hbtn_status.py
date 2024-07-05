#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
            r = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(r)))
            print("\t- content: {}".format(r))
            print("\t- utf8 content: {}".format(r.decode("UTF-8")))
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")

