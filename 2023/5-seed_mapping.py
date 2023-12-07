import re

maps = list(open("2023/5-seed_mapping.txt"))
# seeds = [int(i) for i in re.findall(r"\d+", maps[0])]
seeds_range = [int(i) for i in re.findall(r"\d+", maps[0])]

def get_seed(seeds_range):
    for index in range(len(seeds_range)):
        if index%2 == 1:
            yield seeds_range[index-1], seeds_range[index-1] + seeds_range[index]
    

def complete(map, left, right):
    empty = 0
    for m in map:
        if left <= m[1] + m[2] and right >= m[1]:
            if left - m[1] < 0:
                empty = 
        else:
            map.remove(m)
    leftest = min([i[1] for i in map])
    start = left 

i = 0
for left, right in get_seed(seeds_range):
    flag = True
    for line in maps[1:]:
        map = [int(i) for i in re.findall(r"\d+", line)]
        if left <= map[1] + map[2] and right >= map[1]:
            num = seeds - map[1]
            if num >= 0 and num <= map[2]:
                seeds = map[0] + num
                flag = False
                # print(seeds)
        elif not map and not flag:
            flag = True
            # print(line)
    if i == 0:
        i = seeds
    elif i > seeds:
        i = seeds
print(i)

for index in range(len(seeds_range)):
    if index%2 == 1:
        left = seeds_range[index-1]
        right = seeds_range[index-1] + seeds_range[index]
    for line in maps[3:]:
        map = []
        extract = [int(i) for i in re.findall(r"\d+", line)]
        if extract:
            map.append(extract)
        elif ':' in line:
            complet(map, left, right)
            print(line)
