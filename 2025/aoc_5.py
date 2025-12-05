from sys import stdin


def is_fresh(fresh_ids, id):
    for min_id, max_id in fresh_ids:
        if min_id <= id <= max_id:
            return True
    return False


def part_1(fresh_ids, available_ids):
    cnt = 0
    for id in available_ids:
        if is_fresh(fresh_ids, id):
            cnt += 1
    print(cnt)


def merge_ranges(fresh_ids):
    fresh_ids.sort(key=lambda x: x[0])
    merged_ranges = []
    for min_id, max_id in fresh_ids:
        if not merged_ranges:
            # first one
            merged_ranges.append((min_id, max_id))
        else:
            # update previous if there is overlap
            last_min, last_max = merged_ranges[-1]
            if min_id <= last_max + 1:
                merged_ranges[-1] = (last_min, max(last_max, max_id))
            else:
                merged_ranges.append((min_id, max_id))
    return merged_ranges


def part_2(fresh_ids):
    merged_ranges = merge_ranges(fresh_ids)
    cnt = 0
    for min_id, max_id in merged_ranges:
        cnt += max_id + 1 - min_id
    print(cnt)


if __name__ == "__main__":
    content = stdin.read().strip()
    fresh, available = content.split("\n\n")
    fresh_ids = [tuple(map(int, r.split("-"))) for r in fresh.split("\n")]
    available_ids = [int(id) for id in available.split("\n")]

    part_1(fresh_ids, available_ids)

    part_2(fresh_ids)
