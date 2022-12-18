from collections import deque

data = set(tuple(map(int, i.split(','))) for i in open("AoC_2022_18.txt").read().strip().split('\n'))
dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
part1 = sum((x + dx, y + dy, z + dz) not in data for dx, dy, dz in dirs for x, y, z in data)
air = {(x, y, z) for z in range(20) for y in range(20) for x in range(20)} - data
queue, not_trapped = deque([(0, 0, 0)]), {(0, 0, 0)}
while queue:
    x, y, z = queue.popleft()
    for d in dirs:
        neighbor = (x + d[0], y + d[1], z + d[2])
        if all(0 <= i <= 19 for i in neighbor) and neighbor not in data and neighbor not in not_trapped:
            not_trapped.add(neighbor)
            queue.append(neighbor)
print('Part 1: %d; part 2: %d' % (
    part1, part1 - sum((x + dx, y + dy, z + dz) in data for dx, dy, dz in dirs for x, y, z in air - not_trapped)))
