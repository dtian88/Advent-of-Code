data = [i.split() for i in open("AoC_2022_15.txt").read().strip().split('\n')]
beacons, not_beacons = set(), set()
part2, cols = 0, [[] for _ in range(4000001)]
for sensor in data:
    x, y = int(sensor[2].split('=')[1][:-1]), int(sensor[3].split('=')[1][:-1])
    bx, by = int(sensor[-2].split('=')[1][:-1]), int(sensor[-1].split('=')[1])
    beacons.add((bx, by))
    dist = abs(x - bx) + abs(y - by)
    if y - dist <= 2000000 <= y + dist:
        for offset in range(-(dist - abs(y - 2000000)), dist - abs(y - 2000000) + 1):
            if (x + offset, 2000000) not in beacons:
                not_beacons.add(x + offset)
    for offset in range(max(-dist, -x), min(dist + 1, 4000001 - x)):
        cols[x + offset].append((y - (dist - abs(offset)), y + dist - abs(offset)))
for i, col in enumerate([sorted(col) for col in cols]):
    excluded_range = list(col[0])
    for excluded in col:
        if excluded[0] - 1 <= excluded_range[1] < excluded[1]:
            excluded_range[1] = excluded[1]
        elif excluded[0] - 1 > excluded_range[1]:
            part2 = excluded[0] - 1 + 4000000 * i
            break
    else:
        continue
    break
print('Part 1: %d; part 2: %d' % (len(not_beacons), part2))
