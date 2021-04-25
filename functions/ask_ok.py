#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """Prompts user to provide yes or no input
       Params:
        prompt: Message to prompt user to provide input
        retries: # of times to retry in case of invalid input. 0 or negative value implies no retries allowed.
        reminder: Message to be shown upon invalid input
    
    """
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        if retries > 0:
            print(f'You can try {retries} times!')
        elif retries == 0:
            print('Last try!')

if __name__ == "__main__":
    try:
        ok = ask_ok('Do you really want to quit? ', 10, 'Come on, only yes or no!')
        print("Ok =", ok)
    except ValueError:
        print('Invalid User response')
    