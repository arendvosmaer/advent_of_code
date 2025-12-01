import logging
from sys import stdin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def part_1(rotations):
    state = 50
    cnt = 0
    for r in rotations:
        direction = 1 if r[0] == "R" else -1
        value = int(r[1:])
        state = state + direction * value
        if state == 0:
            cnt += 1
    print(cnt)


def part_2(rotations):
    state = 50
    cnt = 0
    for r in rotations:
        logger.debug(r)
        direction = r[0]
        value = int(r[1:])

        # move state on at a time, count if intermediate state % 100 == 0
        for _ in range(value):
            state = state + 1 if direction == "R" else state - 1
            if state % 100 == 0:
                cnt += 1

        logger.debug(f"state: {state}")
        logger.debug(f"cnt: {cnt}")

    print(cnt)
    # assert cnt == 6475


if __name__ == "__main__":
    inputs = stdin.read().strip().split("\n")

    print("Part 1:")
    part_1(inputs)

    print("Part 2:")
    part_2(inputs)
