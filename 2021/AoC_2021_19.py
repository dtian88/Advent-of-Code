from itertools import permutations

data = open('AoC_2021_19.txt').read().split('\n\n')
scanners = [[tuple(map(int, k.split(','))) for k in list(i.split('\n')[1:])] for i in data]
scanner_positions = {(0, 0, 0)}
beacons = set(scanners[0])
scanners_remaining = set(range(1, 31))
new_correct_scanners = {0}
overlap = {(16, 6), (20, 25), (6, 28), (13, 4), (21, 9), (1, 6), (26, 11), (18, 30), (26, 6), (9, 21), (22, 28), (3, 2),
           (5, 24), (29, 11), (7, 5), (6, 23), (15, 29), (30, 16), (7, 22), (6, 26), (27, 12), (14, 21), (9, 19),
           (6, 16), (13, 0), (12, 27), (22, 26), (28, 22), (5, 1), (13, 3), (24, 5), (1, 5), (22, 7), (8, 6), (23, 6),
           (28, 6), (11, 26), (9, 13), (8, 3), (9, 2), (6, 1), (5, 7), (30, 2), (25, 20), (13, 9), (21, 14), (4, 8),
           (30, 8), (29, 0), (5, 26), (30, 18), (17, 15), (2, 30), (4, 13), (29, 3), (16, 30), (0, 12), (2, 3), (6, 8),
           (12, 0), (11, 8), (20, 24), (11, 29), (8, 4), (23, 4), (2, 9), (10, 12), (4, 23), (12, 10), (0, 29), (3, 13),
           (8, 11), (8, 30), (29, 15), (15, 17), (24, 20), (19, 9), (26, 22), (0, 13), (3, 8), (26, 5), (3, 29)}
directions = set(permutations([1, 1, 1, -1, -1, -1], 3))
orientations = set(permutations(range(3)))


def helper():
    global beacons
    left_temp.discard(r)
    new_temp.add(r)
    updated_beacons = [(c[0] + a[0], c[1] + a[1], c[2] + a[2]) for c in t3]
    scanners[r] = updated_beacons
    beacons = beacons.union(set(updated_beacons))
    raise StopIteration


while scanners_remaining:
    new_temp = set()
    for n in new_correct_scanners:
        for a in scanners[n]:
            t = set((k[0] - a[0], k[1] - a[1], k[2] - a[2]) for k in scanners[n])
            left_temp = scanners_remaining.copy()
            for r in scanners_remaining:
                if (n, r) in overlap:
                    try:
                        for b in scanners[r]:
                            t2 = [(k[0] - b[0], k[1] - b[1], k[2] - b[2]) for k in scanners[r]]
                            for d in directions:
                                for o in orientations:
                                    t3 = [(i[o[0]] * d[0], i[o[1]] * d[1], i[o[2]] * d[2]) for i in t2]
                                    if len(t.intersection(set(t3))) >= 12:
                                        scanner_positions.add(
                                            (a[0] - b[o[0]] * d[0], a[1] - b[o[1]] * d[1], a[2] - b[o[2]] * d[2]))
                                        helper()
                    except StopIteration:
                        continue
            scanners_remaining = left_temp
    new_correct_scanners = new_temp
max_dist = 0  # part 2
for i in scanner_positions:
    for j in scanner_positions:
        max_dist = max(max_dist, abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2])) if i != j else max_dist
print('Part 1: %d; part 2: %d' % (len(beacons), max_dist))
