#!/bin/bash
# send DELETE request to URL passed as first arg, display body of response
curl -sI | grep -i Allow | cut -d ' ' -f 2-
