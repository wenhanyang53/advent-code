
input_text = [i.replace('\n', '') for i in list(open("2023/13-mirror.txt"))]

def analyse(pattern):
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i+1]:
            flag = 0
            if len(pattern[:i+1]) <= len(pattern[i+1:]):
                for j in reversed(range(i)):
                    if pattern[j] != pattern[2*i-j+1]:
                        flag += 1
                if flag == 1:
                    print('A')
                    return 100*(i+1)
            if len(pattern[:i+1]) > len(pattern[i+1:]):
                for j in range(i + 1, len(pattern)):
                    if pattern[j] != pattern[2*i-j+1]:
                        flag += 1
                if flag == 1:
                    print('B')
                    return 100*(i+1)
    for i in range(len(pattern[0]) - 1):
        flag = 0
        for j in range(len(pattern)):
            if pattern[j][i] != pattern[j][i+1]:
                flag += 1
        if flag == 1:
            if len(pattern[0][:i+1]) <= len(pattern[0][i+1:]):
                for n in reversed(range(i)):
                    for m in range(len(pattern)):
                        if pattern[m][n] != pattern[m][2*i-n+1]:
                            flag = 0
                if flag:
                    print('C')
                    return i+1
            if len(pattern[0][:i+1]) > len(pattern[0][i+1:]):
                for n in range(i + 1, len(pattern[0])):
                    for m in range(len(pattern)):
                        if pattern[m][n] != pattern[m][2*i-n+1]:
                            flag = 0
                if flag:
                    print('D')
                    return i+1

pattern = []
total = 0
for i in input_text:
    if '#' in i or '.' in i:
        pattern.append(i)
    else:
        num = analyse(pattern)
        total += num
        pattern = []

print(total)


content = open('2023/13-mirror.txt', 'r').read()

def str_to_num(s: str) -> int:
    res = 0
    for c in s:
        res |= (1 if c == '#' else 0)
        res <<= 1
    return res >> 1

def get_grids() -> list[str]:
    return [grid for grid in content.split('\n\n')]

def parse_grid(grid: str) -> tuple[list[int], list[int]]:
    rows = [row for row in grid.split('\n')]
    cols = [col for col in list(zip(*grid.split('\n')))]

    return ([str_to_num(row) for row in rows], [str_to_num(col) for col in cols])

# [1, 2, 2, 1, 3]
# we need to only get the subarray [1, 2, 2, 1].
"""
[   1,  2,  2,  1,  3   ] len = 5
        i   i+1
i + 1           = 2
5 - (i + 1)     = 3
min_len = 2
subarrays to compare:
    [i + 1 - min_len : i + 1] = [0:2]                       -> [1, 2]
    [i + 1 : i + 1 + min_len].rev = [2:4].rev -> [2, 1].rev -> [1, 2]
"""

#############################################
# ------------- P A R T   1 --------------- #
#############################################
def find_reflection(ls: list[int]) -> int:
    for i in range(len(ls) - 1):
        n1, n2 = ls[i], ls[i + 1]
        if n1 == n2 :
            min_len = min(i + 1, len(ls) - (i + 1))
            sub_1 = ls[i+1 - min_len :i+1]
            sub_2 = ls[i + 1: i+1 + min_len]
            sub_2.reverse()
            if sub_1 == sub_2:
                return i + 1
    return 0

def part_1():
    grids = get_grids()
    res = 0
    for grid in grids:
        rows, cols = parse_grid(grid)
        res += find_reflection(rows) * 100 + find_reflection(cols)
    print(res)

part_1()
