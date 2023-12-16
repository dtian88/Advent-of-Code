from collections import deque

def bfs(start):
  queue, seen, tiles = deque([start]), set(), set()
  while queue:
    beam = queue.popleft()
    tile, direction = [*beam[:2]], beam[2]
    tile[dirs[direction][0]] += dirs[direction][1]
    if 0 <= tile[0] < len(data) and 0 <= tile[1] < len(data[0]):
      for new_direction in chars[data[tile[0]][tile[1]]][direction]:
        if (new_beam := (*tile, new_direction)) not in seen:
          queue.append(new_beam)
          seen.add(new_beam)
          tiles.add(new_beam[:2])
  return len(tiles)


data = open("AoC_2023_16.txt").read().split("\n")
chars = {"\\": {"N": "W", "E": "S", "S": "E", "W": "N"}, "/": {"N": "E", "E": "N", "S": "W", "W": "S"}, ".": {"N": "N", "E": "E", "S": "S", "W": "W"},
         "-": {"N": "EW", "E": "E", "S": "EW", "W": "W"}, "|": {"N": "N", "E": "NS", "S": "S", "W": "NS"}}
dirs = {"N": (0, -1), "S": (0, 1), "W": (1, -1), "E": (1, 1)}

part2 = 0
for i in range(len(data)):
  part2 = max(max(part2, bfs((i, -1, "E"))), bfs((i, len(data[0]), "W")))
for j in range(len(data[0])):
  part2 = max(max(part2, bfs((-1, j, "S"))), bfs((len(data), j, "N")))
  
print("Part 1: %d; part 2: %d" % (bfs((0, -1, "E")), part2))
