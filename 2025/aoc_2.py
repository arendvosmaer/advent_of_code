from sys import stdin


def part_1(ranges):
    sum=0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for id in range(start, end + 1):
            if len(str(id)) % 2 == 1: continue
            mid = len(str(id)) // 2
            left = str(id)[:mid]
            right = str(id)[mid:]
            if left == right:
                sum += id
    print(sum)

def part_2(ranges):
    sum=0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for id in range(start, end + 1):
            mid = len(str(id)) // 2
            for chunk_size in range(1, mid + 1):
                chunks = [str(id)[j:j + chunk_size] for j in range(0, len(str(id)), chunk_size)]
                if all(c == chunks[0] for c in chunks):
                    sum += id
                    break
    print(f"sum: {sum}")


if __name__ == "__main__":
    ranges = stdin.read().strip().split(",")
    print("Part 1:")
    part_1(ranges)

    print("Part 2:")
    part_2(ranges)