#!/usr/bin/env python3

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42) # Define f as incrementor by 42
print(f(0)) # prints 42
print(f(10)) # prints 52

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair:pair[1]) # orders by second element of each list item
print(pairs) 