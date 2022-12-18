from collections import defaultdict, deque


def valve_to_valve(start, end):
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        v, step = queue.popleft()
        if v == end:
            return step
        for c in valves[v][0]:
            if c not in visited:
                queue.append((c, step + 1))
    return -1


def bfs():
    max_pressure = 0
    queue, pressures = deque([('AA', 30, {'AA': 0})]), defaultdict(int)
    while queue:
        current, minute, opened = queue.popleft()
        current_pressure = sum([valves[v][1] * m for v, m in opened.items()])
        max_pressure = max(max_pressure, current_pressure)
        if minute >= 4:
            opened_valves = tuple(sorted(opened.keys()))
            pressures[opened_valves] = max(pressures[opened_valves],
                                           current_pressure - sum([valves[v][1] * 4 for v, m in opened.items()]))
        if current not in opened:
            queue.append((current, minute - 1, opened.copy() | {current: minute - 1}))
            continue
        for adjacent, dist in nonzero[current].items():
            if adjacent not in opened and minute - dist >= 1:
                queue.append((adjacent, minute - dist, opened))
    return max_pressure, max(
        [p1 + p2 for o2, p2 in pressures.items() for o1, p1 in pressures.items() if set(o1) & set(o2) == {'AA'}])


data = open("AoC_2022_16.txt").read().strip().split('\n')
valves, nonzero = dict(), dict()
for i in data:
    j = i.split()
    other_valves = i.split(', ')
    other_valves[0] = other_valves[0][-2:]
    rate = int(j[4].split('=')[1][:-1])
    if rate != 0 or j[1] == 'AA':
        nonzero[j[1]] = dict()
    valves[j[1]] = (other_valves, rate)
for valve in nonzero:
    for valve2 in nonzero:
        if valve != valve2 and valve2 not in nonzero[valve]:
            distance = valve_to_valve(valve, valve2)
            if valve2 != 'AA':
                nonzero[valve][valve2] = distance
            nonzero[valve2][valve] = distance
print('Part 1: %d; part 2: %d' % bfs())

# for i in range(2, len(nonzero_valves) // 2 + 2):
#     for combination in combinations(nonzero_valves, i):
#         combo = set(combination)
#         complement = nonzero_valves.difference(combo)
#         dict1, dict2 = defaultdict(dict), defaultdict(dict)
#         combo.add('AA')
#         complement.add('AA')
#         for valve in combo:
#             for adj in nonzero[valve]:
#                 if adj in combo:
#                     dict1[valve][adj] = nonzero[valve][adj]
#                 if valve != 'AA':
#                     dict1[valve]['AA'] = nonzero['AA'][valve]
#         for valve in complement:
#             for adj in nonzero[valve]:
#                 if adj in complement:
#                     dict2[valve][adj] = nonzero[valve][adj]
#                 if valve != 'AA':
#                     dict1[valve]['AA'] = nonzero['AA'][valve]
#         part2 = max(part2, bfs(dict1, part=True) + bfs(dict2, part=True))
