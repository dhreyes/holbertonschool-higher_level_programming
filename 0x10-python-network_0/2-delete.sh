#!/bin/bash
# send DELETE request to URL passed as first arg, display body of response
curl -sL "$1" DELETE
