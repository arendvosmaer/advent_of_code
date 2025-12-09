from sys import stdin


def surface(a, b, surfaces={}):
    key = str((a, b)) if a < b else str((b, a))
    cached = surfaces.get(key)
    if cached:
        return cached
    xa, ya = a
    xb, yb = b
    x_diff = abs(xa - xb)+1
    y_diff = abs(ya - yb)+1
    res = x_diff * y_diff
    surfaces[key] = res
    return res


def part_1(tiles):
    surfaces={}
    for ta in tiles:
        for tb in tiles:
            surface(ta, tb, surfaces)
    surfaces = sorted(surfaces.items(), key=lambda item: item[1])
    print(surfaces[-1][1])

def is_on_edge():
    pass


def part_2(tiles):
    tiles = sorted(tiles)
    print(tiles)
    max_x=tiles[-1][0]
    tiles=sorted(tiles, key=lambda t: t[1])
    print(tiles)
    max_y=tiles[-1][1]
    print(max_x, max_y)
    floor = [[] for y in range(max_y+2)]
    for y,_ in enumerate(floor):
        for x in range(max_x+3):
            tile="#" if (x,y) in tiles else "."
            floor[y].append(tile)
    print_floor(floor)

def print_floor(floor):
    for y,_ in enumerate(floor):
        print("".join(floor[y]))



if __name__ == "__main__":
    lines = stdin.read().strip().split("\n")
    tiles = [tuple(int(n) for n in line.split(",")) for line in lines]

    part_1(tiles)

    part_2(tiles)
