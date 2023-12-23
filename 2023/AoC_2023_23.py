from collections import defaultdict, deque

data = open("AoC_2023_23.txt").read().split("\n")
data = ["#" * len(data[0])] + data + ["#" * len(data[0])]
for i, line in enumerate(data):
  data[i] = "#" + data[i] + "#"
part1 = 0

start, goal = (1, data[1].index(".")), (len(data) - 2, data[-2].index("."))
moves = {"v": (1, 0), ">": (0, 1)}
queue = deque([(start, {start})])
while queue:
  (i, j), path = queue.popleft()
  if (i, j) == goal:
    part1 = max(part1, len(path) - 1)
    continue
  if data[i][j] not in ".#" and (i + moves[data[i][j]][0], j + moves[data[i][j]][1]) not in path:
    queue.append(((i + moves[data[i][j]][0], j + moves[data[i][j]][1]), {*path, (i + moves[data[i][j]][0], j + moves[data[i][j]][1])}))
  else:
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      if (i + di, j + dj) not in path and data[i + di][j + dj] != "#" and (data[i + di][j + dj] == "." or moves[data[i + di][j + dj]] != (di * -1, dj * -1)):
        queue.append(((i + di, j + dj), {*path, (i + di, j + dj)}))

graph = defaultdict(set)
lengths = {}

for i, line in enumerate(data):
  for j, c in enumerate(line):
    if c != "#":
      for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if data[i + di][j + dj] != "#":
          graph[(i, j)].add((i + di, j + dj))
          lengths[((i, j), (i + di, j + dj))] = 1
          lengths[((i + di, j + dj), (i, j))] = 1

updated = True
while updated:
  updated = False
  for tile, neighbors in graph.items():
    if len(neighbors) == 2:
      updated = True      
      neighbors = list(neighbors)
      for i in range(2):
        graph[neighbors[i]].add(neighbors[1 - i])
        graph[neighbors[i]].remove(tile)
        lengths[(neighbors[i], neighbors[1 - i])] = lengths[(tile, neighbors[i])] + lengths[(tile, neighbors[1 - i])]
      del graph[tile]
      break

def longest_path(i, j, path, length):
  if (i, j) == goal:
    return length
  longest = 0
  for ni, nj in graph[(i, j)]:
    if (ni, nj) not in path:
      path.add((ni, nj))
      longest = max(longest, longest_path(ni, nj, path, length + lengths[((i, j), (ni, nj))]))
      path.remove((ni, nj))
  return longest


print("Part 1: %d; part 2: %d" % (part1, longest_path(*start, {start}, 0)))
