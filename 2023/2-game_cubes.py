import pandas as pd
import re
import numpy as np

input_bags = {'red': 12, 'green': 13, 'blue': 14}

df = pd.read_csv("puzzle/2-game_cubes.csv", header=None, index_col=False, sep=";")
df[0] = df[0].apply(lambda x: x.split(":")[-1])
# print(df)

def collect(x, biggest):
    try:
        red = re.findall(r"\d+ red", x)[0].split(' ')[0]
        if int(red) > biggest['red']:
            biggest['red'] = int(red)
    except:
        pass
    try:
        green = re.findall(r"\d+ green", x)[0].split(' ')[0]
        if int(green) > biggest['green']:
            biggest['green'] = int(green)
    except:
        pass
    try:
        blue = re.findall(r"\d+ blue", x)[0].split(' ')[0]
        if int(blue) > biggest['blue']:
            biggest['blue'] = int(blue)
    except:
        pass    

    return biggest

def compare(input_bag: dict, game: dict):
    for k in input_bag.keys():
        if game[k] > input_bag[k]:
            return False
    return True

def multiply (x: dict):
    i = 1
    for k in x.keys():
        i *= x[k]
    return i

# x = '2 blue, 14 red'
# biggest = {'red': 0, 'green': 0, 'blue': 0}
# arr = np.full((5, ), biggest)
# df["total"] = arr
# print(collect(x, biggest))

rows, columns = df.shape
i = 0
for r in range(rows):
    biggest = {'red': 0, 'green': 0, 'blue': 0}
    for c in range(columns):
        biggest = collect(df.iloc[r,c], biggest)
    # if compare(input_bags, biggest):
    #     i += (r+1)
    i += multiply(biggest)

print(i)