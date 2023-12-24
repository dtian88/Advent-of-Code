# 88/2211
data = open("AoC_2023_10.txt").read().split('\n')
for i, line in enumerate(data):
  if "S" in line:
    start = [i, line.index("S")]

turns = {"F": {"N": "E", "W": "S"}, "L": {"S": "E", "W": "N"}, "J": {"S": "W", "E": "N"}, "7": {"N": "W", "E": "S"}}
dirs = {"N": (0, -1), "S": (0, 1), "W": (1, -1), "E": (1, 1)}

current = [start[0] + 1, start[1]]
tiles = 1
loop_path = {tuple(start), tuple(current)}
direction = "S"
while data[current[0]][current[1]] != "S":
  if (c := data[current[0]][current[1]]) not in "|-":
    direction = turns[c][direction]
  current[dirs[direction][0]] += dirs[direction][1]
  tiles += 1
  loop_path.add(tuple(current))

part2 = 0
for i, line in enumerate(data):
  inside = 0
  for j, c in enumerate(line):
    inside ^= (i, j) in loop_path and c in "|JLS"
    part2 += (i, j) not in loop_path and inside

print("Part 1: %d; part 2: %d" % (tiles // 2, part2))


# part1 = part2 = 0
# data = open("AoC_2023_10.txt").read().split('\n')
# start = [0, 0]
# for i, l1 in enumerate(data):
#   for j, l2 in enumerate(l1):
#     if l2 == "S":
#       start = [i, j]

# current = [start[0] + 1, start[1]]
# tiles = 1
# loop_path = [tuple(start), tuple(current)]
# direction = "S"
# while data[current[0]][current[1]] != "S":
#   if data[current[0]][current[1]] == "F":
#     if direction == "N":
#       direction = "E"
#       current[1] += 1
#     elif direction == "W":
#       direction = "S"
#       current[0] += 1
#   elif data[current[0]][current[1]] == "L":
#     if direction == "S":
#       direction = "E"
#       current[1] += 1
#     elif direction == "W":
#       direction = "N"
#       current[0] -= 1
#   elif data[current[0]][current[1]] == "J":
#     if direction == "S":
#       direction = "W"
#       current[1] -= 1
#     elif direction == "E":
#       direction = "N"
#       current[0] -= 1
#   elif data[current[0]][current[1]] == "7":
#     if direction == "N":
#       direction = "W"
#       current[1] -= 1
#     elif direction == "E":
#       direction = "S"
#       current[0] += 1
#   elif data[current[0]][current[1]] == "|":
#     if direction == "N":
#       current[0] -= 1
#     elif direction == "S":
#       current[0] += 1
#   elif data[current[0]][current[1]] == "-":
#     if direction == "W":
#       current[1] -= 1
#     elif direction == "E":
#       current[1] += 1
#   tiles += 1
#   loop_path.append(tuple(current))


# loop_path_set = set(loop_path)
# part2 = 1
# seen = []

# def recur(pos):
#   if pos[0] < 0 or pos[0] >= len(data) or pos[1] < 0 or pos[1] >= len(data[0]) or pos in seen[-1] or pos in loop_path_set:
#     return
#   seen[-1].add(pos)
#   for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#       recur((pos[0] + dx, pos[1] + dy))


# current_dir = "S"
# inside_dir = "W"
# for i, p in enumerate(loop_path[:-1]):
#   if inside_dir == "N":
#     check_tile = (p[0] - 1, p[1])
#   elif inside_dir == "S":
#     check_tile = (p[0] + 1, p[1])
#   elif inside_dir == "E":
#     check_tile = (p[0], p[1] + 1)
#   else:
#     check_tile = (p[0], p[1] - 1)
#   if 0 <= check_tile[0] < len(data) and 0 <= check_tile[1] < len(data[0]) and check_tile not in loop_path_set and not any(check_tile in s for s in seen):
#     seen.append(set())
#     recur(check_tile)
#   if data[p[0]][p[1]] == "F":
#     if inside_dir == "N":
#       inside_dir = "W"
#     elif inside_dir == "S":
#       inside_dir = "E"
#     elif inside_dir == "W":
#       inside_dir = "N"
#     else:
#       inside_dir = "S"
#   elif data[p[0]][p[1]] == "L":
#     if inside_dir == "N":
#       inside_dir = "E"
#     elif inside_dir == "S":
#       inside_dir = "W"
#     elif inside_dir == "W":
#       inside_dir = "S"
#     else:
#       inside_dir = "N"
#   elif data[p[0]][p[1]] == "J":
#     if inside_dir == "N":
#       inside_dir = "W"
#     elif inside_dir == "S":
#       inside_dir = "E"
#     elif inside_dir == "W":
#       inside_dir = "N"
#     else:
#       inside_dir = "S"
#   elif data[p[0]][p[1]] == "7":
#     if inside_dir == "N":
#       inside_dir = "E"
#     elif inside_dir == "S":
#       inside_dir = "W"
#     elif inside_dir == "W":
#       inside_dir = "S"
#     else:
#       inside_dir = "N"

#   if inside_dir == "N":
#     check_tile = (p[0] - 1, p[1])
#   elif inside_dir == "S":
#     check_tile = (p[0] + 1, p[1])
#   elif inside_dir == "E":
#     check_tile = (p[0], p[1] + 1)
#   else:
#     check_tile = (p[0], p[1] - 1)
#   if 0 <= check_tile[0] < len(data) and 0 <= check_tile[1] < len(data[0]) and check_tile not in loop_path_set and not any(check_tile in s for s in seen):
#     seen.append(set())
#     recur(check_tile)

# print("Part 1: %d; part 2: %d" % (tiles // 2, sum(len(s) for s in seen)))
