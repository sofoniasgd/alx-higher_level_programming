#!/bin/bash
# a Bash script that takes in a URL, sends a request to that \
# URL, and displays the size of the body of the response
# 	-s silent mode
# 	-o /dev/null discard the output cuz we're not interested
# 	-w ${size_download} custom output format
curl -s -o /dev/null -w "%{size_download}\n" "$1"
