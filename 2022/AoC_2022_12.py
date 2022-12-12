from collections import deque


def bfs(r, c):
    visited, d = {(r, c)}, deque([(r, c, 0)])
    while d:
        x, y, n = d.popleft()
        if (x, y) == end:
            return n
        for x2, y2 in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if (x2, y2) not in visited and 0 <= x2 < len(data) and 0 <= y2 < len(data[0]) and ord(data[x2][y2]) - ord(
                    data[x][y]) <= 1:
                visited.add((x2, y2))
                d.append((x2, y2, n + 1))
    return float('inf')


raw = open("AoC_2022_12.txt").read().strip()
first_line = raw.find("\n") + 1
start = raw.find("S") // first_line, raw.find("S") % first_line
end = raw.find("E") // first_line, raw.find("E") % first_line
data = raw.replace("S", "a").replace("E", "z").split("\n")
part1 = part2 = float('inf')
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "a":
            res = bfs(i, j)
            if (i, j) == start:
                part1 = res
            part2 = min(part2, res)
print('Part 1: %s; part 2: %s' % (part1, part2))
