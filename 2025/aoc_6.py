from sys import stdin


def calc(columns):
    gt = 0
    for c in columns:
        op = c[-1]
        if op == "+":
            for f in c[:-1]:
                gt += int(f)
        else:
            p = 1
            for f in c[:-1]:
                p = p * int(f)
            gt += p
    return gt


def part_1(lines):
    columns = []
    for l in lines:
        fields = l.strip().split()
        if not columns:
            columns = [[f] for f in fields]
        else:
            for i, f in enumerate(fields):
                columns[i].append(f)
    gt = calc(columns)
    print(gt)


def part_2(lines):
    grid = [list(l) for l in lines]
    spaces_to_add = len(grid[0]) - len(grid[-1])
    grid[-1] += [" "] * spaces_to_add

    columns = [[]]
    column_index = 0
    for idx, val in enumerate(grid[0]):
        if is_separator(grid, idx):
            column_index += 1
            columns.append([])
            continue
        number = number_at(grid, idx)
        columns[column_index].append(number)
    gt = 0
    for idx, operator in enumerate(lines[-1].split()):
        if operator == "+":
            for n in columns[idx]:
                gt += n
        else:
            p = 1
            for n in columns[idx]:
                p *= n
            gt += p
    print(gt)


def is_separator(grid, idx):
    for line in grid:
        if line[idx] != " ":
            return False
    return True


def number_at(grid, idx):
    number = ""
    for line in grid[:-1]:
        number += line[idx]
    return int(number)


if __name__ == "__main__":
    lines = stdin.read().strip().split("\n")

    part_1(lines)

    part_2(lines)
