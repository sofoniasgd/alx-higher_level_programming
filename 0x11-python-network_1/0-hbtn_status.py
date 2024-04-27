#!/usr/bin/python3
"""0. What's my status? #0(Task 0)"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        body = html.decode("utf-8")
        print("\t- utf8 content: {}".format(body))
