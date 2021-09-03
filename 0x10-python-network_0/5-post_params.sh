#!/bin/bash
# send POST request to passed URL. Sent two vars in request
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
