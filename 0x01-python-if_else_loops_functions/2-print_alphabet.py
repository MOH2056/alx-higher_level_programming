#!/usr/bin/python3
for s in range(97, 123):
    if s in [101, 113]:
        continue
    print("{}".format(chr(s)), end='')
