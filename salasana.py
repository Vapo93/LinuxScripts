#!/bin/python3
import sys
import random
import string

default_len = 8
def get_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

pituus = default_len
try:
    pituus = sys.argv[1]

except IndexError as e:
    pituus = str(default_len)


pituus = int(pituus) if pituus.isdigit() else default_len

print(get_random_string(pituus))
