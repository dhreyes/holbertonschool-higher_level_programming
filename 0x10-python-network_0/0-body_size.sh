#!/bin/bash
# takes in a URL, send request to URL, display size of body to response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f
