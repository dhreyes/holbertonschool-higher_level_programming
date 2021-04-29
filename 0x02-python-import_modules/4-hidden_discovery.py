#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lists = dir(hidden_4)
    for string in lists:
        if string[0:2] != "__":
            print("{:s}".format(string))
