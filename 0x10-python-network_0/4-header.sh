#!/bin/bash
# Get the response body for a given URL and append a header variable with valuei.
curl -s -H "X-School-User-Id: 98" "$1"
