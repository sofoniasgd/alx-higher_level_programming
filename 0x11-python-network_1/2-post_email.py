#!/usr/bin/python3
"""2. POST an email #0(Task 1)"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        body = html.decode("utf-8")
        print(body)
