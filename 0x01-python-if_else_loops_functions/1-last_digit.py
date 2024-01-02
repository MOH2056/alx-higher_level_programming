#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
store = -(abs(number) % 10)
if (store > 5):
    print(f"Last digit of {number} is {store} and is greater than 5")
elif (store == 0):
    print(f"Last digit of {number} is {store} and is 0")
elif (store < 6 and store != 0):
    print(f"Last digit of {number} is {store} and is less than 6 and not 0")
