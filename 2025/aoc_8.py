from sys import stdin
from typing import List, Tuple
import time
from math import hypot, prod


def part_2(junction_boxes):
    distances = {}
    for jb1 in junction_boxes:
        for jb2 in junction_boxes:
            if jb1 == jb2:
                continue
            distance(jb1, jb2, distances)
    pairs = sorted(distances.items(), key=lambda item: item[1])
    circuits = [[jb] for jb in junction_boxes]
    while len(circuits) >= 2:
        jb1, jb2 = pairs.pop(0)[0]
        c1, c2 = [], []
        for c in circuits:
            if jb1 in c:
                c1 = c
            if jb2 in c:
                c2 = c
        if c1 != c2:
            c1 += c2
            circuits.remove(c2)
    print(jb1[0] * jb2[0])


def part_1(junction_boxes):
    distances = {}
    for jb1 in junction_boxes:
        for jb2 in junction_boxes:
            if jb1 == jb2:
                continue
            distance(jb1, jb2, distances)
    pairs = sorted(distances.items(), key=lambda item: item[1])
    circuits = [[jb] for jb in junction_boxes]
    connection_count = 0
    while connection_count < 1000:
        jb1, jb2 = pairs.pop(0)[0]
        c1, c2 = [], []
        for c in circuits:
            if jb1 in c:
                c1 = c
            if jb2 in c:
                c2 = c
        if c1 != c2:
            c1 += c2
            circuits.remove(c2)
        connection_count += 1
    circuits.sort(key=lambda c: -len(c))
    print(len(circuits))
    print(prod([len(c) for c in circuits[:3]]))


def distance(jb1, jb2, distances):
    first, second = (jb1, jb2) if jb1 < jb2 else (jb2, jb1)
    key = (first, second)
    cached = distances.get(key)
    if cached:
        return cached
    diff = [a - b for a, b in zip(first, second)]
    dist = hypot(*diff)
    distances[key] = dist
    return dist


if __name__ == "__main__":
    lines = stdin.read().strip().split("\n")
    junction_boxes = [tuple([int(n) for n in line.split(",")]) for line in lines]

    # part_1(junction_boxes)

    part_2(junction_boxes)
