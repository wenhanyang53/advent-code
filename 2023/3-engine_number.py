import pandas as pd
import re
import math as m

df = pd.read_csv("puzzle/3-engine_number.csv", header=None, index_col=False, sep=";")
# print(df)

class engine():

    def __init__(self, schematic) -> None:
        self.schematic = schematic
        self.rows, _ = self.schematic.shape
        self.columns = len(self.schematic.iloc[0, 0])

    def get_element(self, position: list) -> str:
        element =  self.schematic.iloc[position[0], 0][position[1]]
        return element
    
    def get_scan_area(self, length: int, row: int, position:int) -> list:
        area = []
        for j in range(-1,2):
            for i in range(-1, length+1):
                p = [min(max(row+j, 0), self.rows-1), 
                     min(max(position+i, 0), self.columns-1)]
                if p not in area:
                    area.append(p)
        for l in range(length):
            area.remove([row, position+l])
        
        return area
    
    def scan(self) -> list:
        total = 0
        total_pair = {}
        for r in range(self.rows):
            nums = re.finditer(r"\d+", self.schematic.iloc[r, 0])
            if nums:
                for n_group in nums:
                    n = n_group.group()
                    print("start the number: ", n)
                    length = len(n)
                    position = n_group.start()
                    area = self.get_scan_area(length, r, position)
                    for ia in area:
                        element = self.get_element(ia)
                        if element == "*":
                            pos = tuple(ia)
                            if pos not in total_pair.keys():
                                total_pair[pos] = []
                                total_pair[pos].append(int(n))
                                break
                            else:
                                total_pair[pos].append(int(n))
                                break
                        # if re.findall(r"[^\.\d\n\r]", element):
                        #     total += int(n)
                        #     break

                   
        return sum(m.prod(p) for p in total_pair.values() if len(p)==2)
    
engine = engine(df)
my = engine.scan()
print(my)

def other_solution():
    board = list(open("puzzle/3-engine_number.txt"))
    chars = {(r, c): [] for r in range(140) for c in range(140)
                        if board[r][c] not in '01234566789.'}

    for r, row in enumerate(board):
        for n in re.finditer(r'\d+', row):
            edge = {(r, c) for r in (r-1, r, r+1)
                        for c in range(n.start()-1, n.end()+1)}

            for o in edge & chars.keys():
                chars[o].append(int(n.group()))

    # return chars.values()
    print(sum(sum(p)    for p in chars.values()),
        sum(m.prod(p) for p in chars.values() if len(p)==2))

