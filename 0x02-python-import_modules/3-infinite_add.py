#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    addnt = 0
    for i in range(1, len(argv)):
        addnt += int(argv[i])
    print("{}".format(addnt))
