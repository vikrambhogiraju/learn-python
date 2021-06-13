#!/usr/bin/env python3

def fib(n):  # Write Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, b+a
    return result

if __name__ == "__main__":
    print("type(fib):", type(fib))
    print("fib(2000) =", fib(2000))
    f = fib
    print("f(100) =", f(100))
    f100 = fib(100)
    print("f100 = ", f100)

