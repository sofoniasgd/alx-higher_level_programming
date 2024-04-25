#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
# and displays the body of the response
# 	-X explicitly state GET method
# 	-o /dev/null discard the output cuz we're not interested
# 	-w ${size_download} custom output format
http_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")
# echo "code is ${http_code}"
if [ "$http_code" -eq 200 ]; then
	body=$(curl -s -o - "$1")
	echo "${body}"
fi
