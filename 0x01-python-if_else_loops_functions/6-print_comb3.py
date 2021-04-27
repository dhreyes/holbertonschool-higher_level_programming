#!/usr/bin/python3
for ones in range(0, 10):
    for tens in range(ones + 1, 10):
        print("{:d}{:d}".format(ones, tens), end="")
        if ones * 10 + tens != 89:
            print(", ", end="")
print("")
