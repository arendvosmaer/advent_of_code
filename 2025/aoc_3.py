from sys import stdin
from typing import List


def max_joltage(batteries: List[str], n: int) -> str:
    if n == 0 or not batteries:
        return ""
    max_index = batteries.index(max(batteries[: len(batteries) - (n - 1)]))
    max_value = batteries[max_index]
    return max_value + max_joltage(batteries[max_index + 1 :], n - 1)


def part_1(banks: List[str]):
    sum = 0
    for bank in banks:
        batteries = list(bank)
        # # find highest value digit, that is not the last
        # first = batteries.index(max(batteries[:-1]))
        # second = batteries.index(max(batteries[first+1:]))
        # sum += int(batteries[first]+ batteries[second])
        sum += int(max_joltage(batteries, 2))
        print(sum)


def part_2(banks):
    sum = 0
    for bank in banks:
        batteries = list(bank)
        sum += int(max_joltage(batteries, 12))
        print(sum)


if __name__ == "__main__":
    inputs = stdin.read().strip().split("\n")
    # inputs = ["123", # 23
    #           "451" # 51
    #           ]
    part_1(inputs)  # 16973
    part_2(inputs)
