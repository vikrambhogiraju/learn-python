#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):  # Write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, b+a
    print()

if __name__ == "__main__":
    fib(2000)
    f = fib
    f(100)

