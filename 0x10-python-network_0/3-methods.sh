#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sI "$1" | grep -i '^Allow:' | awk '{print substr($0, 8)}'
