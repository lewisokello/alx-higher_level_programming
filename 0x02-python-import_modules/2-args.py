#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    q = len(argv)
    print("{:d} {:s}{:s}".format(q - 1, "argument" if q <= 2 else "arguments",
                                 "." if q == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
