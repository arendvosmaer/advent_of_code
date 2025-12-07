from sys import stdin
from typing import List, Tuple
import time


def count_paths(grid, source, cache={}):
    cached = cache.get(str(source))
    if cached:
        return cached
    x, y = source
    if y >= len(grid) - 1:
        return 1
    if x < 0 or x >= len(grid[y]):
        return 0
    if grid[y][x] == "^":
        count = count_paths(grid, (x - 1, y + 1)) + count_paths(grid, (x + 1, y + 1))
        cache[str(source)] = count
        return count
    count = count_paths(grid, (x, y + 1))
    cache[str(source)] = count
    return count


def propagate(
    grid: List[List[str]], beam: Tuple[int, int], cache={}
) -> List[List[str]]:
    key = str(beam)
    cached = cache.get(key)
    if cached:
        return cached

    x, y = beam

    if x < 0 or x >= len(grid[0]):
        return grid

    if grid[y][x] == "^":
        grid = propagate(grid, (x - 1, y + 1))
        grid = propagate(grid, (x + 1, y + 1))
        cache[key] = grid
        return grid

    grid[y][x] = "|"

    print_grid(grid, x, y)
    cache[key] = grid

    if y >= len(grid) - 1:
        return grid

    return propagate(grid, (x, y + 1))


def count_splits(grid: List[List[str]]) -> int:
    cnt = 0
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            if field == "^":
                if grid[y - 1][x] == "|":
                    cnt += 1
    return cnt


first = True


def print_grid(grid, x, y):
    global first
    if not first:
        # move cursor to updated field and only print new character "|"
        print(f"\033[{y+1};{x+1}H|", end="", flush=True)
        time.sleep(0.001)
        return
    first = False
    print("\033[2J\033[H", end="")  # Clear screen and move to home
    for row in grid:
        print("".join(row))
    print(flush=True)


def part_1(grid):
    grid = [[f for f in r] for r in grid]
    source = (grid[0].index("S"), 1)
    grid = propagate(grid, source)
    print(count_splits(grid))


def part_2(grid):
    source = (grid[0].index("S"), 1)
    paths = count_paths(grid, source)
    print(paths)


if __name__ == "__main__":
    lines = stdin.read().strip().split("\n")
    grid = [list(line) for line in lines]

    part_1(grid)

    part_2(grid)
