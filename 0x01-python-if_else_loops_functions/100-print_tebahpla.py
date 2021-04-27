#!/usr/bin/python3
count = 0
swap = ord('A') - ord('a')
for alpha in range(ord('z'), ord('a') - 1, -1):
    if count % 2 == 1:
        print("{}".format(chr(alpha + swap)), end="")
    else:
        print("{}".format(chr(alpha)), end="")
    count += 1
