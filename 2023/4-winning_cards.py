import pandas as pd
import re
import math

cards = list(open("puzzle/4-winning_cards.txt"))
instance = dict.fromkeys(range(1, 203), 1)

def search(cards):
    score = 0
    for i, c in enumerate(cards):
        l = []
        c1 = c.split("|")[0].split(": ")[-1]
        c2 = c.split("|")[1]
        winning_numbers = re.findall(r"\d+",  c1)
        my_numbers = re.findall(r"\d+", c2)
        for w in winning_numbers:
            if w in my_numbers:
                l.append(w)
        if l:
            # score += math.pow(2, len(l)-1)
            for ll in range(len(l)):
                instance[i+ll+2] += instance[i+1]
    return sum(instance.values())

print(search(cards=cards))