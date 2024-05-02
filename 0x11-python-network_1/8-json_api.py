#!/usr/bin/python3
"""4. What's my status? #1(Task 4)"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})
    try:
        json_txt = r.json()
    except Exception as e:
        print("Not a valid JSON")
    else:
        if len(json_txt) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_txt['id'], json_txt['name']))
