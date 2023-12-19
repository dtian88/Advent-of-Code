def find_vertices(part2=False):
  x = y = edge_points = 0
  points = []
  for line in open("AoC_2023_18.txt").read().split("\n"):
    if not part2:
      direction, distance, _ = line.split()
      distance = int(distance)
    else:
      _, _, temp = line.split()
      distance = int(temp[2:-2], 16)
      direction = ["R", "D", "L", "U"][int(temp[-2])]
    edge_points += distance - 1
    if direction in "UD":
      x += distance * (1 if direction == "D" else -1)
    else:
      y += distance * (1 if direction == "R" else -1)
    points.append((x, y))
  return points[::-1], edge_points


def find_area(vertices, edge_points):
  sum1 = sum2 = 0
  for i in range(len(vertices) - 1):
    sum1 += vertices[i][0] *  vertices[i + 1][1]
    sum2 += vertices[i][1] *  vertices[i + 1][0]
  sum1 += vertices[-1][0] * vertices[0][1]
  sum2 += vertices[0][0] * vertices[-1][1]
  return (abs(sum1 - sum2) + len(vertices) + edge_points) // 2 + 1


print("Part 1: %d; part 2: %d" % (find_area(*find_vertices()), find_area(*find_vertices(True))))



# from collections import defaultdict

# data = open("AoC_2023_18.txt").read().split("\n")
# part1 = part2 = 0

# def find_volume(part2=False):
#   x, y, v = 0, 0, 0
#   points = defaultdict(set)
#   insides = {}
#   current_dir = "U"
#   inside_dir = "UR"
#   horizontals = {}
#   for line in data:
#     if not part2:
#       direction, amount, _ = line.split()
#       amount = int(amount)
#     else:   
#       _, _, temp = line.split()
#       amount = int(temp[2:-2], 16)
#       direction = ["R", "D", "L", "U"][int(temp[-2])]
#     if direction == "U":
#       if current_dir == "L":
#         if inside_dir == "UL":
#           inside_dir = "UR"
#         elif inside_dir == "DR":
#           inside_dir = "DL"
#       else:
#         assert current_dir == "R"
#         if inside_dir == "UR":
#           inside_dir = "UL"
#         elif inside_dir == "DL":
#           inside_dir = "DR"
#     elif direction == "D":
#       if current_dir == "L":
#         if inside_dir == "UR":
#           inside_dir = "UL"
#         elif inside_dir == "DL":
#           inside_dir = "DR"
#       else:
#         assert current_dir == "R"
#         if inside_dir == "UL":
#           inside_dir = "UR"
#         elif inside_dir == "DR":
#           inside_dir = "DL"
#     elif direction == "L":
#       if current_dir == "U":
#         if inside_dir == "UL":
#           inside_dir = "DL"
#         elif inside_dir == "DR":
#           inside_dir = "UR"
#       else:
#         assert current_dir == "D"
#         if inside_dir == "UR":
#           inside_dir = "DR"
#         elif inside_dir == "DL":
#           inside_dir = "UL"
#     else:
#       if current_dir == "U":
#         if inside_dir == "UR":
#           inside_dir = "DR"
#         elif inside_dir == "DL":
#           inside_dir = "UL"
#       else:
#         assert current_dir == "D"
#         if inside_dir == "DR":
#           inside_dir = "UR"
#         elif inside_dir == "UL":
#           inside_dir = "DL"
#     insides[(x, y)] = inside_dir
#     current_dir = direction

#     if direction in "UD":
#       for _ in range(amount):
#         x += 1 if direction == "D" else -1
#         points[x].add((y, 0))
#         if (x, y) not in insides:
#           insides[(x, y)] = inside_dir
#     else:
#       prev_y = y
#       y += amount if direction == "R" else -amount
#       points[x].add((y, 1))
#       horizontals[(x, prev_y)] = y
#       horizontals[(x, y)] = prev_y

#   x = [(p, list(sorted(points[p]))) for p in sorted(points.keys())]

#   for i, y in x:
#     inside = True
#     start = True
#     for z in range(len(y) - 1):
#       if horizontals.get((i, y[z][0]), -1) == y[z + 1][0]:
#         v += y[z + 1][0] - y[z][0]
#       else:
#         if start:
#           inside = "R" in insides[(i, y[z][0])]
#           start = False
#         if inside:
#           v += y[z + 1][0] - y[z][0]
#         else:
#           v += 1
#         if not (z < len(y) - 2 and horizontals.get((i, y[z + 1][0]), -1) == y[z + 2][0] and (len(set(insides[(i, y[z + 1][0])]) | set(insides[(i, y[z + 2][0])])) == 3)):
#           inside = not inside
#     v += 1
#   return v

# print("Part 1: %d; part 2: %d" % (find_volume(), find_volume(True)))
