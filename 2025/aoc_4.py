from sys import stdin
from typing import List

def neighbours(d, x, y) -> List[str]:
    max_y = len(d)
    max_x = len(d[0])
    

if __name__ == "__main__":
    d = {}
    lines = stdin.read().strip().split("\n")
    lines = [".@.", "@@@", "@@."]
    for y, line in enumerate(lines):
        d[y] = {}
        fields = list(line)
        for x, field in enumerate(fields):
            d[y][x] = True if field == "@" else False
    print(d)
