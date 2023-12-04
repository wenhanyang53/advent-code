import pandas as pd
import re 

df = pd.read_csv("puzzle/1-calibration_value.csv", header=None, names=["input"], index_col=False)
# print(df)

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def convert(x: str):
    x = x.lower()
    for i, n in enumerate(numbers):
        if n in x:
            index = x.find(n)
            if index != -1:
                x = x[:index+1] + str(i+1) + x[index+1:]
            index = x.rfind(n)
            if index != -1:
                x = x[:index+1] + str(i+1) + x[index+1:]

    return x

x = 'five2gmxjthkksfiveonerj2nine'
print(convert(x))

df["convert"] = df["input"].apply(lambda x: convert(x))
df['digital'] = df["convert"].apply(lambda x: int(re.findall(r"\d", str(x))[0]) * 10 + int(re.findall(r"\d", str(x))[-1]))

print(df.head)
print(df["digital"].sum())