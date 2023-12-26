
input_text = [i.replace('\n', '') for i in list(open("2023/14-tilt_rocks.txt"))]

def calculate_load(input_text):
    total = 0
    for i in range(len(input_text[0])):
        count = 0
        start = 0
        for j in range(len(input_text)):
            if input_text[j][i] == 'O':
                count += 1
            if input_text[j][i] == '#':
                for n in range(count):
                    total += 1 * (len(input_text) - start - n)
                start = (j + 1)
                count = 0
            if j == len(input_text) - 1:
                for n in range(count):
                    total += 1 * (len(input_text) - start - n)
                count = 0
    return total

print(calculate_load(input_text))

def tilt_n(input_text):
    result = [''] * len(input_text)
    for i in range(len(input_text[0])):
        count = 0
        start = 0
        for j in range(len(input_text)):
            if input_text[j][i] == 'O':
                count += 1
            if input_text[j][i] == '#':
                for n in range(count):
                    result[start + n] += 'O'
                for n in range(j - count - start):
                    result[start + count + n] += '.'
                result[j] += '#'
                start = (j + 1)
                count = 0
            if j == len(input_text) - 1:
                for n in range(count):
                    result[start + n] += 'O'
                for n in range(j - count - start + 1):
                    result[start + count + n] += '.'
                count = 0
    return result

def tilt_s(input_text):
    result = [''] * len(input_text)
    for i in range(len(input_text[0])):
        count = 0
        start = 0
        for j in range(len(input_text)):
            if input_text[j][i] == 'O':
                count += 1
            if input_text[j][i] == '#':
                for n in range(count):
                    result[j - count + n] += 'O'
                for n in range(j - count - start):
                    result[start + n] += '.'
                result[j] += '#'
                start = (j + 1)
                count = 0
            if j == len(input_text) - 1:
                for n in range(count):
                    result[j - count + n + 1] += 'O'
                for n in range(j - count - start + 1):
                    result[start + n] += '.'
                count = 0
    return result

def tilt_w(input_text):
    result = []
    for i in range(len(input_text)):
        count = 0
        start = 0
        line = ''
        for j in range(len(input_text[0])):
            if input_text[i][j] == 'O':
                count += 1
            if input_text[i][j] == '#':
                for n in range(count):
                    line += 'O'
                for n in range(j - count - start):
                    line += '.'
                line += '#'
                start = (j + 1)
                count = 0
            if j == len(input_text[0]) - 1:
                for n in range(count):
                    line += 'O'
                for n in range(j - count - start + 1):
                    line += '.'
                count = 0
        result.append(line)
    return result

def tilt_e(input_text):
    result = []
    for i in range(len(input_text)):
        count = 0
        start = 0
        line = ''
        for j in range(len(input_text[0])):
            if input_text[i][j] == 'O':
                count += 1
            if input_text[i][j] == '#':
                for n in range(j - count - start):
                    line += '.'
                for n in range(count):
                    line += 'O'
                line += '#'
                start = (j + 1)
                count = 0
            if j == len(input_text[0]) - 1:
                for n in range(j - count - start + 1):
                    line += '.'
                for n in range(count):
                    line += 'O'
                count = 0
        result.append(line)
    return result

def cycle(input_text, num):
    result0 = input_text
    for i in range(num):
        result1 = tilt_n(result0)
        result2 = tilt_w(result1)
        result3 = tilt_s(result2)
        result4 = tilt_e(result3)
        if result0 == result4:
            print(num)
            break
        else:
            result0 = result4
    return resul4

result = cycle(input_text, 1000000000)
print(calculate_load(result))