#!/usr/bin/python3
"""4. What's my status? #1(Task 4)"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
