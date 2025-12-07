from sys import stdin


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
    grid = [list(l) for l in lines[:-1]]

    columns = [[]]
    column_index = 0
    for idx, val in enumerate(grid[0]):
        if is_separator(grid, idx):
            column_index += 1
            columns.append([])
            continue
        number = number_at(grid, idx)
        columns[column_index].append(number)

    for idx, operator in enumerate(lines[-1].split()):
        columns[idx].append(operator)

    print(calc(columns))


def is_separator(grid, idx):
    for line in grid:
        if line[idx] != " ":
            return False
    return True


def number_at(grid, idx):
    number = ""
    for line in grid:
        number += line[idx]
    return int(number)


if __name__ == "__main__":
    lines = stdin.read().strip().split("\n")

    part_1(lines)

    part_2(lines)
