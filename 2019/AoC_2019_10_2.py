import math
from collections import OrderedDict

data = ['.#.####..#.#...#...##..#.#.##.',
'..#####.##..#..##....#..#...#.',
'......#.......##.##.#....##..#',
'..#..##..#.###.....#.#..###.#.',
'..#..#..##..#.#.##..###.......',
'...##....#.##.#.#..##.##.#...#',
'.##...#.#.##..#.#........#.#..',
'.##...##.##..#.#.##.#.#.#.##.#',
'#..##....#...###.#..##.#...##.',
'.###.###..##......#..#...###.#',
'.#..#.####.#..#....#.##..#.#.#',
'..#...#..#.#######....###.....',
'####..#.#.#...##...##....#..##',
'##..#.##.#.#..##.###.#.##.##..',
'..#.........#.#.#.#.......#..#',
'...##.#.....#.#.##........#..#',
'##..###.....#.............#.##',
'.#...#....#..####.#.#......##.',
'..#..##..###...#.....#...##..#',
'...####..#.#.##..#....#.#.....',
'####.#####.#.#....#.#....##.#.',
'#.#..#......#.........##..#.#.',
'#....##.....#........#..##.##.',
'.###.##...##..#.##.#.#...#.#.#',
'##.###....##....#.#.....#.###.',
'..#...#......#........####..#.',
'#....#.###.##.#...#.#.#.#.....',
'.........##....#...#.....#..##',
'###....#.........#..#..#.#.#..',
'##...#...###.#..#.###....#.##.']

above = below = left = right = False
angles = dict()
i = 25
j = 22
maximum = 0
for k in range(len(data)):
  for l in range(len(data[k])):
    if data[k][l] == '#' and (i != k or j != l):
      if l == j:
        if i > k:
	        angle = 0
        else:
	        angle = math.pi
        if angle not in angles:
          angles[angle] = []
        angles[angle].append((abs(i - k), (l, k)))
      else:
        angle = math.atan((i - k) / (l - j))
        if j > l:
          angle += math.pi
        angle = math.pi/2 - angle
        if angle < 0:
          angle += 2 * math.pi
        if angle not in angles:
          angles[angle] = []
        angles[angle].append((math.pow(i - k, 2) + math.pow(j - l, 2), (l, k)))

ordered = OrderedDict(sorted(angles.items()))
for a in ordered.values():
  sorted(a)
count = 0
found = (-1, -1)
while count < 200:
  for key in ordered:
    if count == 200:
      break
    if ordered[key]:
      found = ordered[key].pop(0)[1]
      count += 1
print(100 * found[0] + found[1])