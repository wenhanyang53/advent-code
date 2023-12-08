import re
import itertools
from math import lcm

input_text = list(open("2023/8-navigate_map.txt"))
instructions = itertools.cycle(input_text[0][:-1])

map = {}
start = {}
for i in input_text[2:]:
    k = i.split(' = ')[0]
    v = re.findall(r'\w+', i.split(' = ')[1])
    map[k] = v

    if k[2] == "A":
        start[k] = "..."

count = 0

def solve(k, v):
    count = 0
    while True:
        i = next(instructions)
        if i == "R":
            k = map[k][1]
        if i == "L":
            k = map[k][0]
        count += 1
        if k.endswith("Z"):
            break
    return count

result = []
for k, v in start.items():
    count = solve(k, v)
    result.append(count)

print(lcm(*result))
        