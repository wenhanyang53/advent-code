import numpy as np
import re
from copy import deepcopy
import math

input_text = list(open("2023/9-predict_value.txt"))

total = []

def part1(input_text):
    for i in input_text:
        arr = i.split(' ')
        arr = np.array([int(i) for i in arr])
        arr = np.append(arr, 0) # place holder
        arr_all = deepcopy(arr)
        arr_all = arr_all.reshape(1,-1)
        num = 1
        length = arr.size
        while True:
            arr =  arr[1:] - arr[:-1]
            arr = np.append(arr, 0) # place holder
            arr_all = np.vstack([arr_all, arr])
            num += 1
            if np.array_equal(arr[:length - num -1], np.zeros(length - num -1)):
                arr_all[arr_all.shape[0]-1][length - num] = 0 # make last value to be 0
                break
        for j in reversed(range(arr_all.shape[0] - 1)):
            arr_all[j][1:] = arr_all[j][:-1] + arr_all[j+1][:-1]
        print(arr_all)
        total.append(arr_all[0][length-1])
    return total

# print(sum(part1(input_text)))

def part2(input_text):
    for i in input_text:
        arr = i.split(' ')
        arr = np.array([int(i) for i in arr])
        arr = np.concatenate(([0], arr), axis=0) # place holder
        arr_all = deepcopy(arr)
        arr_all = arr_all.reshape(1,-1)
        num = 1
        length = arr.size
        while True:
            arr =  arr[1:] - arr[:-1]
            arr = np.concatenate(([0], arr), axis=0) # place holder
            arr_all = np.vstack([arr_all, arr])
            num += 1
            if np.array_equal(arr[num: ], np.zeros(length - num)):
                arr_all[arr_all.shape[0]-1][num-1] = 0 # make first value to be 0
                break
            
        for j in reversed(range(arr_all.shape[0] - 1)):
            arr_all[j][num -2: -1] = arr_all[j][num - 1:] - arr_all[j+1][num - 1:]
            num -= 1
        print(arr_all)
        total.append(arr_all[0][0])
    return total

print(sum(part2(input_text)))