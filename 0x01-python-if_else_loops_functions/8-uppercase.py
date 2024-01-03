#!/usr/bin/python3
def uppercase(str):
    for iterator in str:
        semi = iterator
        if ord(semi) >= 97 and ord(semi) <= 122:
            semi = chr(ord(semi) - 32)
        print("{}".format(semi), end='')
    print()
