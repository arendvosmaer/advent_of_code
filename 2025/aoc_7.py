from sys import stdin
from typing import List, Tuple
import sys
import time
sys.setrecursionlimit(100000)

def part_1(grid):
    grid = [[f for f in r] for r in grid]
    source = (grid[0].index("S"), 1)
    grid = propagate(grid, [source])
    print(count_splits(grid))


def part_2(lines):
    pass


def propagate(
    grid: List[List[str]], beams: List[Tuple[int, int]]
) -> List[List[str]]:
    if not beams:
        return grid
    print_grid(grid)
    x,y = beams.pop(0)
    
    if x < 0 or x >= len(grid[0]) or grid[y][x]=="|":
        return propagate(grid, beams)
    
    grid[y][x]="|"

    if y+1 >= len(grid):
        return propagate(grid, beams)

    next = grid[y+1][x]
    if next == ".":
        beams.append((x, y+1))
    else:
        beams.append((x-1, y+1))
        beams.append((x+1, y+1))
    return propagate(grid, beams)


def print_grid(grid, animate=False):
    if animate:
        time.sleep(10 / len(grid) / len(grid[0]))
        print("\033[2J\033[H", end="")  # Clear terminal and move cursor to top
    for row in grid:
        print("".join(row))


def count_splits(grid: List[List[str]]) -> int:
    cnt = 0
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            if field == "^":
                if grid[y - 1][x] == "|":
                    cnt += 1
    return cnt


if __name__ == "__main__":
    with open("/Users/arend/git/advent_of_code/2025/aoc_7_input_example.txt", "r") as file:
        lines = file.read().strip().split("\n")
    lines = stdin.read().strip().split("\n")
    grid = [list(line) for line in lines]

    part_1(grid)

    part_2(grid)
