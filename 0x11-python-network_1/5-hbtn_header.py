#!/usr/bin/python3
"""5. Response header value #1(Task 5)"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            r = requests.get(sys.argv[1])
        except Exception:
            pass
        else:
            print(r.headers['X-Request-Id'])
