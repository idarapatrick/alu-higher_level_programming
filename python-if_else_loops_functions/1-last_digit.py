#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

num_str = str(number)
last_digit = num_str[-1]

if int(last_digit) > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5 \n")
elif int(last_digit) == 0:
    print(f"Last digit of {number} is {last_digit} and is 0 \n")
elif int(last_digit) < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0 \n")
