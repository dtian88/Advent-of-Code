from math import lcm

directions, data = open("AoC_2023_8.txt").read().split('\n\n')
graph = {line.split(" = ")[0]: (line.split(" = ")[1].split(", ")[0][1:], line.split(" = ")[1].split(", ")[1][:-1])
         for line in data.split('\n')}
nodes, node_steps = [node for node in graph if node[-1] == "A"], []
part1_index = nodes.index("AAA")
for n in nodes:
  steps = 0
  for d in directions * 100:
    steps += 1
    if (n := graph[n][d == "R"])[-1] == "Z":
      node_steps.append(steps)
      break

print('Part 1: %d; part 2: %d' % (node_steps[part1_index], lcm(*node_steps)))
