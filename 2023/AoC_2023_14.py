data = list(map(list, open("AoC_2023_14.txt").read().split("\n")))
seen, cycle, cycles, loads = set(), 0, {}, {}

while (new := "".join("".join(line) for line in data)) not in seen:
  seen.add(new)
  cycles[new] = cycle
  loads[cycle] = sum([line.count("O") * (len(data) - j) for j, line in enumerate(data)])
  cycle += 1

  for i in range(len(data)):
    for j in range(len(data[0])):
      for ii in range(i - 1, -1, -1):
        if data[ii + 1][j] == "O" and data[ii][j] == ".":
          data[ii + 1][j] = "."
          data[ii][j] = "O"
        else:
          break
  
  if cycle == 1:
    part1 = sum([line.count("O") * (len(data) - j) for j, line in enumerate(data)])

  for j in range(len(data[0])):
    for i in range(len(data)):
      for jj in range(j - 1, -1, -1):
        if data[i][jj + 1] == "O" and data[i][jj] == ".":
          data[i][jj + 1] = "."
          data[i][jj] = "O"
        else:
          break

  for i in range(len(data) - 1, -1, -1):
    for j in range(len(data[0])):
      for ii in range(i + 1, len(data)):
        if data[ii - 1][j] == "O" and data[ii][j] == ".":
          data[ii - 1][j] = "."
          data[ii][j] = "O"
        else:
          break

  for j in range(len(data[0]) - 1, -1, -1):
    for i in range(len(data)):
      for jj in range(j + 1, len(data[0])):
        if data[i][jj - 1] == "O" and data[i][jj] == ".":
          data[i][jj - 1] = "."
          data[i][jj] = "O"
        else:
          break

print("Part 1: %d; part 2: %d" % (part1, loads[(1000000000 - cycles[new]) % (cycle - cycles[new]) + cycles[new]]))
