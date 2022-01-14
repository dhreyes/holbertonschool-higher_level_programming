#!/usr/bin/python3
"""
Take in a URL, sends a request to the URL and display value of the
X-Request-Id variable found in the header of response
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
