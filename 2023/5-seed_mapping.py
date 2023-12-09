import re
import numpy as np
from copy import deepcopy

maps = list(open("2023/5-seed_mapping.txt"))
# seeds = [int(i) for i in re.findall(r"\d+", maps[0])]
seeds_range = [int(i) for i in re.findall(r"\d+", maps[0])]

def get_seed(seeds_range):
    for index in range(len(seeds_range)):
        if index%2 == 1:
            yield seeds_range[index-1], seeds_range[index-1] + seeds_range[index]


# modify the straight line based on the real mapping
def mapping(map, input_data):
    output = deepcopy(input_data)
    for i in input_data.keys():
        left = i[0]
        right = i[1]
        for m in map:
            if left < m[1] and right <= m[1] + m[2] and right >= m[1]:
                out_left = m[1]
                out_right = right
                output[(out_left, out_right)] = m[1] - m[0]
                output[(left, out_left)] = 0
                output.pop((left, right))
                right = out_left
            if left >= m[1] and right <= m[1] + m[2]:
                out_left = left
                out_right = right
                output[(out_left, out_right)] = m[1] - m[0]
            if left >= m[1] and left <= m[1] + m[2] and right > m[1] + m[2]:
                out_left = left
                out_right = m[1] + m[2]
                output[(out_left, out_right)] = m[1] - m[0]
                output[(out_right, right)] = 0
                output.pop((left, right))
                left = out_right
    
    return output

# map = [[60, 56, 37],[56, 93, 4]]
# input_data = {(46, 57): 0, (78, 81): 0}
# print(mapping(map, input_data))

def transform(input_data):
    output = {}
    for k, v in input_data.items():
        output[k[0]-v, k[1]-v] = 0

    return output

# input_data = {(78, 81): -4, (56, 57): -4, (46, 56): 0}
# print(transform(input_data))

def get_min(input_data):
    result = []
    for k, v in input_data.items():
        result.append(k[0]-v)
    return result

# input_data = {(78, 81): -4, (56, 57): -4, (46, 56): 0}
# print(get_min(input_data))

# i = 0
# for left, right in get_seed(seeds_range):
#     flag = True
#     for line in maps[1:]:
#         map = [int(i) for i in re.findall(r"\d+", line)]
#         if left <= map[1] + map[2] and right >= map[1]:
#             num = seeds - map[1]
#             if num >= 0 and num <= map[2]:
#                 seeds = map[0] + num
#                 flag = False
#                 # print(seeds)
#         elif not map and not flag:
#             flag = True
#             # print(line)
#     if i == 0:
#         i = seeds
#     elif i > seeds:
#         i = seeds
# print(i)

score = []
for index in range(len(seeds_range)):
    if index%2 == 1:
        left = seeds_range[index-1]
        right = seeds_range[index-1] + seeds_range[index]
        input_data = {(left, right): 0} # c value, y=x+c
        map = []
        for line in maps[3:]:
            extract = [int(i) for i in re.findall(r"\d+", line)]
            if extract:
                map.append(extract)
            elif ':' in line:
                input_data = mapping(map, input_data)
                map = []
                input_data = transform(input_data)
                print(input_data)
                print(line)
        
        result = get_min(input_data)
        score.append(min(result))

print(min(score))