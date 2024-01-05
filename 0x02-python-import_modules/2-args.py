#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    dis = len(argv) -1
    if dis < 1:
        print("{} arguments.".format(dis))
    elif dis == 1:
        print("{} argument:".format(dis))
    else:
        print("{} arguments".format(dis))

    for x in range(dis):
        print("{}: {:s}".format(x + 1, argv[x +1]))
