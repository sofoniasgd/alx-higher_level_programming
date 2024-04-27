#!/usr/bin/python3
"""4. What's my status? #1(Task 4)"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
