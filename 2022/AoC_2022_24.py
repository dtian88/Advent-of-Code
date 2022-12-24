# 46/82
from collections import deque


def add_blizzard():
    global left, right, up, down
    left = {(r, (c - 2) % (w - 2) + 1) for r, c in left}
    right = {(r, c % (w - 2) + 1) for r, c in right}
    up = {((r - 2) % (h - 2) + 1, c) for r, c in up}
    down = {(r % (h - 2) + 1, c) for r, c in down}
    blizzards.append(left | right | up | down)


data = open("AoC_2022_24.txt").read().split('\n')
part1 = part2 = 0
left, right, up, down = (set() for _ in range(4))
dirs = {'<': left, '>': right, '^': up, 'v': down}
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char in dirs:
            dirs[char].add((i, j))
start, end, h, w = (0, data[0].index('.')), (len(data) - 1, data[-1].index('.')), len(data), len(data[0])
queue, visited, blizzards, trip = deque([(start, 0)]), set(), [], 0
add_blizzard()
while queue:
    (y, x), m = queue.popleft()
    if y == h - 1 and data[y][x] == '.':
        if trip == 0:
            queue = deque([(end, m + 1)])
            part1 = m + 1
            trip += 1
            continue
        elif trip == 2:
            part2 = m + 1
            break
    elif y == 0 and data[y][x] == '.' and trip == 1:
        queue = deque([(start, m + 1)])
        trip += 1
        continue
    if m == len(blizzards) - 1:
        add_blizzard()
    for pos in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1), (y, x)):
        if pos[0] < h and data[pos[0]][pos[1]] != '#' and pos not in blizzards[m + 1] and (pos, m + 1) not in visited:
            visited.add((pos, m + 1))
            queue.append((pos, m + 1))
print('Part 1: %d; part 2: %d' % (part1, part2))
