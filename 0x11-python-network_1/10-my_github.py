#!/usr/bin/python3
"""9. My GitHub!(task 9)"""

import requests
import sys

# Python script that takes GitHub credentials
# (username and password) and uses the GitHub API to display user id
if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    headers = {
        "Authorization": f"token {token}",
            }
    url = f"https://api.github.com/users/{username}"

    data = requests.get(url, headers=headers).json()

    # get id from json
    print(data.get("id"))
