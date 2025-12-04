from sys import stdin


def neighbour_roll_count(d, x, y, distance=1) -> int:
    max_y = len(d) - 1
    max_x = len(d[0]) - 1
    cnt = 0
    for ny in range(y - distance, y + distance + 1):
        if ny < 0 or ny > max_y:
            continue
        for nx in range(x - distance, x + distance + 1):
            if nx < 0 or nx > max_x:
                continue
            if nx == x and ny == y:
                continue
            if d[ny][nx]:
                cnt += 1
    return cnt


def list_removable_fields(d):
    fields = []
    for y in d:
        for x in d[y]:
            if d[y][x] and neighbour_roll_count(d, x, y) < 4:
                fields.append((x, y))
    return fields


def part_1(d):
    print(len(list_removable_fields(d)))


def part_2(d):
    cnt = 0
    while True:
        fields = list_removable_fields(d)
        if len(fields) == 0:
            break
        for x, y in fields:
            cnt += 1
            d[y][x] = False
    print(cnt)


if __name__ == "__main__":
    lines = stdin.read().strip().split("\n")

    d: dict[int, dict[int, bool]] = {}
    for y, line in enumerate(lines):
        d[y] = {}
        fields = list(line)
        for x, field in enumerate(fields):
            d[y][x] = True if field == "@" else False

    part_1(d)
    part_2(d)
