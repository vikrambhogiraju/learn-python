#!/usr/bin/env python3

def cheeseshop(kind, *args, **kwargs):
    print("--Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print('*' * 40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])

def test_cheeseshop():
    cheeseshop('Limburger', "It's very runny, sir.",
                "It's really very VERY runny, sir.",
                shopkeeper="Michael Palin",
                client="John Cleese",
                sketch="Cheese Shop Sketch")

if __name__ == "__main__":
    test_cheeseshop()