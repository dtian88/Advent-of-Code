# 61/888
from z3 import Real, Solver

data = open("AoC_2023_24.txt").read().split("\n")
part1 = 0
minimum, maximum = 2e14, 4e14
stones = []

for line in data:
  position, velocity = (list(map(int, p.split(", "))) for p in line.split(" @ "))
  stones.append((position, velocity, velocity[1] / velocity[0], -1, velocity[1] / velocity[0] * (-position[0]) + position[1]))

for i, (pos1, vel1, a1, b1, c1) in enumerate(stones):
  for j in range(i + 1, len(stones)):
    pos2, vel2, a2, b2, c2 = stones[j]
    if a1 * b2 - a2 * b1 == 0 or a1 * b2 - a2 * b1 == 0:
      continue
    intersection = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1), (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
    if all(minimum <= intersection[k] <= maximum for k in range(2)) and all((intersection[l] - [pos1, pos2][k][l]) * [vel1, vel2][k][l] > 0 for k in range(2) for l in range(2)):
      part1 += 1

x, y, z, vx, vy, vz = (Real(var) for var in ["x", "y", "z", "vx", "vy", "vz"])
solver = Solver()
for i in range(4):
  (px, py, pz), (pvx, pvy, pvz) = stones[i][:2]
  t = Real(f"t{i}")
  solver.add(t >= 0)
  solver.add(x + vx * t == px + pvx * t)
  solver.add(y + vy * t == py + pvy * t)
  solver.add(z + vz * t == pz + pvz * t)
solver.check()

print("Part 1: %d; part 2: %d" % (part1, sum(solver.model().eval(v).as_long() for v in [x, y, z])))