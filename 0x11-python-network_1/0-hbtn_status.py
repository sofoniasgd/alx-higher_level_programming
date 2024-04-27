#!/usr/bin/python3
"""0. What's my status? #0(Task 0)"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print(html)
