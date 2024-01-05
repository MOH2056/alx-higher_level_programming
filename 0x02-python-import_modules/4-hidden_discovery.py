#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    var = dir()
    for i in range(len(var)):
        if var[i][:2] != "__":
            print("{:s}".format(var[i]))
