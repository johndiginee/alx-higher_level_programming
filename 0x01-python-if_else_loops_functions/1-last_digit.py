#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = repr(number)
last = int(number_string[-1:])

if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))

elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last))

else:
    print("Last digit of {} is {} and is less\
than 6 and not 0".format(number, last))
