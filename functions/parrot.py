#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """
    Example function that accepts one required argument (voltage) 
        and three optional arguments (stage, action, type)
    """
    print("-- This parrot wouldn't", action, end=' ')
    print(" if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def test_parrot():
    # Valid ways function can be called
    # Functions can be called using keyword arguments of the form kwarg=value. 
    # Other kind of args are called positional arguments
    # keyword arguments must always follow positional arguments 
    #   and should match the args accepted by function
    parrot(1000) # 1 pos arg
    parrot(voltage=1000) # 1 kw arg
    parrot(voltage=10000000, action='VOOOOM') # 2 kw args
    parrot(action='VOOOOM', voltage=10000000) # 2 kw args
    parrot('a million', 'bereft of life', 'jump') # 3 pos args
    parrot('a thousand', state='pushing up the daisies') # 1 pos, 1 kw arg

    # Invalid ways - Uncomment each to see errors
    # parrot() # required argument missing
    # parrot(voltage=5.0, 'dead') non-kw arg after a kw arg
    # parrot(110, voltage=220) # duplicate value for the same arg
    # parrot(actor='John Cleese') # unknown kw arg and required arg missing

if __name__ == "__main__":
    test_parrot()