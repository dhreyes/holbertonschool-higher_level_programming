#!/usr/bin/python3
if __name__ == "__main__":
    sum = 0
    from sys import argv
    for idx in range(1, len(argv)):
        sum += int(argv[idx])
    print("{:d}".format(sum))
