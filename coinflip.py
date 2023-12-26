import random

def coinflipping():
    flip = ("Heads", "Tails")
    choice = random.choice(flip)
    print(f"{choice}")
    print("-----------")
    aftereffect()

def aftereffect():
    afterimage = ("x", "X", "r", "R")
    exits = None
    while exits not in afterimage:
        exits = input("type x to exit\ntype r to reflip: ")
        if exits == 'r' or exits =='R':
            print("-----------")
            coinflipping()
        elif exits == 'x' or exits == 'X':
            print("exiting")
            exit()

coinflipping()
