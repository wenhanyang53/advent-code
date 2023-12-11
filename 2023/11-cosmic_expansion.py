
input_text = [i.replace('\n', '') for i in list(open("2023/11-cosmic_expansion.txt"))]

# expand horizonte
def expand_horizontal(input_text):
    row = []
    for index, i in enumerate(input_text):
        if '#' in i:
            continue
        else:
            row.append(index)
    return row

row = expand_horizontal(input_text)

def expand_vertical(input_data):
    cols = []
    for i in range(len(input_data[0])):
        counter = 0
        for index, j in enumerate(input_data):
            if j[i] == '.':
                counter += 1
            if counter == len(input_data):
                cols.append(i)
            
    return cols

col = expand_vertical(input_text)

galaxies = []
for i, line in enumerate(input_text):
    for j, pos in enumerate(line):
        if pos == '#':
            galaxies.append([i, j])

sum = 0
expansion = 1000000

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        r_count = 0
        for r in row:
            if (r > galaxies[i][0] and r < galaxies[j][0]) or (r > galaxies[j][0] and r < galaxies[i][0]):
                r_count += 1
        c_count = 0
        for c in col:
            if (c > galaxies[i][1] and c < galaxies[j][1]) or c > galaxies[j][1] and c < galaxies[i][1]:
                c_count += 1

        step = abs(galaxies[j][0]-galaxies[i][0]) + abs(galaxies[j][1]-galaxies[i][1]) + (r_count + c_count) * (expansion - 1)
        sum += step

print(sum)

