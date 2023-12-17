from heapq import heappop, heappush

def min_heat_loss(part2=False):
  dists = {}
  queue=[(0, 0, 0, 0, 0)]  # distance (minimum heat loss) from start, i, j, direction, moves in that direction
  while queue:
    dist, i, j, direction, moves = heappop(queue)
    if (i, j) == (len(data) - 1, len(data[0]) - 1):
      if moves >= 4 or not part2:
        return dist
    for new_dir, (di, dj) in enumerate([[1, 0], [0, 1], [-1, 0], [0, -1]]):
      new_moves, new_i, new_j = (moves + 1) if direction == new_dir else 1, i + di, j + dj
      if (new_moves <= 3 and not part2 or \
        new_moves <= 10 and not (0 < moves < 4 and new_dir != direction) and part2) and \
        (new_dir + 2) % 4 != direction and (0 <= new_i < len(data) and 0 <= new_j < len(data[0])):
          key = (new_i, new_j, new_dir, new_moves)
          if (new_dist := dist + int(data[new_i][new_j])) < dists.get(key, 1e100):
            dists[key] = new_dist
            heappush(queue, (new_dist, *key))


data = open("AoC_2023_17.txt").read().split("\n")
print("Part 1: %d; part 2: %d" % (min_heat_loss(), min_heat_loss(True)))
