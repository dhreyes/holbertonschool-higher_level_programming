#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv
    ac = len(av)
    if ac == 1:
        print("0 arguments.")
    elif ac == 2:
        print("{:d} argument:".format(ac - 1))
    else:
        print("{:d} arguments:".format(ac - 1))
    for idx in range(1, ac):
        print("{:d}: {:s}".format(idx, av[idx]))
