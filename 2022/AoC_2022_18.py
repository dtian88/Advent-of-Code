from collections import deque

data = set(tuple(map(int, i.split(','))) for i in open("AoC_2022_18.txt").read().strip().split('\n'))
o = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
part1 = sum((x + a, y + b, z + c) not in data for a, b, c in o for x, y, z in data)
air = {(x, y, z) for z in range(20) for y in range(20) for x in range(20)}.difference(data)
queue, not_trapped = deque([(0, 0, 0)]), {(0, 0, 0)}
while queue:
    x, y, z = queue.popleft()
    for offset in o:
        neighbor = (x + offset[0], y + offset[1], z + offset[2])
        if all(0 <= i <= 19 for i in neighbor) and neighbor not in data and neighbor not in not_trapped:
            not_trapped.add(neighbor)
            queue.append(neighbor)
print('Part 1: %d; part 2: %d' % (
    part1, part1 - sum((x + a, y + b, z + c) in data for a, b, c in o for x, y, z in air.difference(not_trapped))))
