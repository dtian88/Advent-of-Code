from collections import defaultdict, deque
from itertools import combinations

data = open("AoC_2023_11.txt").read().split('\n')
empty_rows = {i for i, line in enumerate(data) if all(c == "." for c in line)}
empty_cols = {j for j in range(len(data[0])) if all(c == "." for c in [line[j] for line in data])}
part1 = part2 = 0


def bfs(original, seen):
  queue = deque([(original, 0)])
  while queue:
    g, num = queue.popleft()
    if g in galaxies:
      dists[original][g] = num
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      new_g = (g[0] + dx, g[1] + dy)
      if 0 <= new_g[0] < len(data) and 0 <= new_g[1] < len(data[0]) and new_g not in seen:
        seen.add(new_g)
        queue.append((new_g, num + 1))


galaxies = {(i, j) for j in range(len(data[0])) for i in range(len(data)) if data[i][j] == "#"}
dists = defaultdict(dict)
for galaxy in galaxies:
  bfs(galaxy, {galaxy})

for g1, g2 in combinations(galaxies, 2):
  for r in empty_rows:
    if g1[0] < r < g2[0] or g2[0] < r < g1[0]:
      part1 += 1
      part2 += 999999
  for c in empty_cols:
    if g1[1] < c < g2[1] or g2[1] < c < g1[1]:
      part1 += 1
      part2 += 999999
  part1 += dists[g1][g2]
  part2 += dists[g1][g2]

print('Part 1: %d; part 2: %d' % (part1, part2))
