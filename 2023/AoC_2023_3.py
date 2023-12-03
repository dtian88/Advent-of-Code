from math import prod

data = open("AoC_2023_3.txt").read().split('\n')
part1 = part2 = 0
nums = set()
for i in range(len(data)):
  prev = 0
  for j in range(len(data[i])):
    if j < prev:
      continue
    if data[i][j].isdigit():
      end = j + 1
      while end < len(data[i]) and data[i][end].isdigit():
        end += 1
      prev = end
      symbol = False
      for x in (-1, 0, 1):
        for y in range(-1, end - j + 1):
          if not (x == 0 and y == 0) and 0 <= i + x < len(data) and 0 <= j + y < len(data[0]) and data[i + x][j + y] != "." and not data[i + x][j + y].isdigit():
            symbol = True
      if symbol:
        part1 += int(data[i][j:end])
        nums.add((i, j, end - 1, int(data[i][j:end])))
for i in range(len(data)):
  for j in range(len(data[i])):
    if data[i][j] == "*":
      n = set()
      for x in (-1, 0, 1):
        for y in (-1, 0, 1):
          if x == 0 and y == 0:
            continue
          for num in nums:
            if num[0] == i + x and num[1] <= j + y <= num[2]:
              n.add(num[3])
      if len(n) == 2:
        part2 += prod(n)  

print('Part 1: %d; part 2: %d' % (part1, part2))
