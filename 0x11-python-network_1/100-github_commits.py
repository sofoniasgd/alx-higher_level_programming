#!/usr/bin/python3
"""10. Time for an interview!(task 10)"""

import requests
import sys

# list 10 commits (from the most recent to oldest)
# of the repository “rails” by the user “rails”

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    data = requests.get(url).json()

    # get sha and author from json
    count = 0
    commit_dict = {}
    for key in data:
        if count < 10:
            if key.get("sha"):
                sha = key.get("sha")
            if key.get("commit"):
                commit = key.get("commit")
                auth = commit.get("author")
            if sha not in commit_dict.keys():
                commit_dict[sha] = auth.get("name")
                count += 1
    for key in commit_dict:
        print(f"{key}: {commit_dict[key]}")
