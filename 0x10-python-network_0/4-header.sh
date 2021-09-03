#!/bin/bash
# take in URL as argument, display body of response, variable must be sent with value 98
curl -s --header "X-HolbertonSchool-User-Id: 98" $1
