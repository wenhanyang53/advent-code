
input_text = list(open("2023/10-pipe.txt"))

pipes = []
for i in input_text:
    pipe = []
    for j in i:
        if j!= '\n':
            pipe.append(j)
        if j == 'S':
            col_s = i.index('S')
            row_s = len(pipes)
    edge_col = len(pipe) - 1
    pipes.append(pipe)
edge_row = len(pipes) - 1

map = { '|': {'row': [-1, 1]},
        '-': {'col': [-1, 1]},
        'L': {'row': [-1], 'col': [1]},
        'J': {'row': [-1], 'col': [-1]},
        '7': {'row': [1], 'col': [-1]},
        'F': {'row': [1], 'col': [1]},
        '.': {'row': [0], 'col': [0]},
        'S': {'row': [-1, 1], 'col': [-1, 1]}
        }

def is_connected(a: dict, b: dict) -> bool:
    # dict of character, row and column
    k_a = list(a.keys())[0]
    k_b = list(b.keys())[0]
    for map_ka, map_va in map[k_a].items():
        for map_kb, map_vb in map[k_b].items():
            if map_ka == map_kb:
                for v_a in map_va:
                    for v_b in map_vb:
                        if v_a + a[k_a][map_ka] == b[k_b][map_kb] and v_b + b[k_b][map_kb] == a[k_a][map_ka]:
                            return True
    return False

# print(is_connected({'7': {'row': 1, 'col': 3}}, {'S': {'row': 1, 'col': 2}}))

def get_area(row: int, col: int, edge_row: int, edge_col: int) -> list:
    return [[max(row-1, 0), col], [min(row+1, edge_row), col], [row, max(col-1, 0)], [row, min(col+1, edge_col)]]

dist = {(row_s, col_s): 0}
path = [[row_s, col_s]]
while len(path) > 0:
    new = path.pop(0)
    for cor in get_area(*new, edge_row, edge_col):
        a = pipes[new[0]][new[1]]
        b = pipes[cor[0]][cor[1]]
        if is_connected({a: {'row': new[0], 'col': new[1]}}, {b: {'row': cor[0], 'col': cor[1]}}) and tuple(cor) not in dist:
            path.append(cor)
            dist[tuple(cor)] = dist[tuple(new)] + 1

print(dist)
print('Part 1 :', max([d for v,d in dist.items()]))

insides = 0
for row, pipe in enumerate(pipes):
    for col, char in enumerate(pipe):
        if (row, col) not in dist:
            counter = [(row, l) for l in range(col) if (row, l) in dist and pipes[row][l] not in ['-','J','L']]
            if len(counter) % 2 == 1:
                insides += 1
                print(counter)

print(insides)