#!/bin/bash
# take in URL as argument, display body of response, variable must be sent with value 98
curl -sI "$1" -H "X-HolbertonSchool-User-Id: 98"
