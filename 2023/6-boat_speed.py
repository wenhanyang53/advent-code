import re

maps = list(open("2023/6-boat_speed.txt"))
time = [int(i) for i in re.findall(r"\d+", maps[0].replace(' ', ''))]
distance = [int(i) for i in re.findall(r"\d+", maps[1].replace(' ', ''))]

margin = 1
for i in range(len(time)):
    num = 0
    for j in range(time[i]+1):
        if j*(time[i]-j) > distance[i]:
            num += 1
    margin *= num

print(margin)