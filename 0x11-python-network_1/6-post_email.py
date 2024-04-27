#!/usr/bin/python3
"""4. What's my status? #1(Task 4)"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
        print(r.text)
