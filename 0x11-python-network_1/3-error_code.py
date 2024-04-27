#!/usr/bin/python3
"""3. Error code #0(Task 3)"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            body = html.decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
