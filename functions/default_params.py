#!/usr/bin/env python3

"""Functions that demonstrate behavior of default params to functions"""

# Default param can be a value of a variable but is evaluated at the time of definition
i = 5
def check_default_arg_value(arg=i):  # evaluates to def f(arg=5):
    print('arg in check_default_arg_value() = ', arg)

print('i =', i) # prints i = 5
check_default_arg_value()  # prints 5 as default param is 5

i = 6
print('i =', i) # prints i = 6
check_default_arg_value()  # prints 5 again as changes to i after definition of f has no effect 
                           # on the default param of f

# Also, default value is evaluated only once. So, when the default is a mutable object 
# such as list, dict or instances of classes, the earlier values take effect

# Function accumulate_arg() below accumulates the args passed to it
def accumulate_arg(a, L=[]):
    L.append(a)
    return L

print('accumulate_arg(1):', accumulate_arg(1)) # prints [1]
print('accumulate_arg(2):', accumulate_arg(2)) # prints [1, 2]
print('accumulate_arg(3):', accumulate_arg(3)) # prints [1, 2, 3]

