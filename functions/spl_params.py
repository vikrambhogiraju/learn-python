#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def std_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kw_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kw_only):
    print(pos_only, standard, kw_only)

def test_std_arg():
    print("Testing std_arg()")
    std_arg(2) # prints 2
    std_arg(arg=2) # prints 2

def test_pos_only_arg():
    print("Testing pos_only_arg()")
    pos_only_arg(1) # prints 1
    # pos_only_arg(arg=1) # fails with unexpected keyword argument error. Uncomment to see error

def test_kw_only_arg():
    print("Testing kw_only_arg")
    # kw_only_arg(2) # fails with takes 0 positional argument... error. Uncomment to see error
    kw_only_arg(arg=3) # prints 3

def test_combined_example():
    print("Testing combined example")
    # combined_example(1, 2, 3) # Fails with takes 2 positional arguments ... error. Uncomment to see error
    combined_example(1, 2, kw_only=3) # prints 1, 2, 3
    combined_example(1, standard=2, kw_only=3) # prints 1, 2, 3
    # combined_example(pos_only=1, standard=2, kw_only=3) # Fails with unexpected keyword argument pos_only

if __name__ == "__main__":
    test_pos_only_arg()
    test_std_arg()
    test_kw_only_arg()
    test_combined_example()


