from functools import cache

@cache
def dp(s, g, s_idx, g_idx):
  if s_idx >= len(s):
    return g_idx == len(g)
  if g_idx == len(g):
    return "#" not in s[s_idx:]
  n = 0
  if s[s_idx] != "#":
    n += dp(s, g, s_idx + 1, g_idx)
  if s[s_idx] != "." and s_idx + g[g_idx] <= len(s) and "." not in s[s_idx:s_idx + g[g_idx]] and (s + ".")[s_idx + g[g_idx]] != "#":
    n += dp(s, g, s_idx + g[g_idx] + 1, g_idx + 1)
  return n


data = open("AoC_2023_12.txt").read().split("\n")
part1 = part2 = 0
for i, line in enumerate(data):
  springs, temp = line.split()
  groups = tuple(map(int, temp.split(",")))
  part1 += dp(springs, groups, 0, 0)
  part2 += dp("?".join([springs] * 5), groups * 5, 0, 0)

print("Part 1: %d; part 2: %d" % (part1, part2))


# def recur(s, g, a):
#   groups = []
#   ii = -1
#   group_num = 0
#   if a == len(s):
#     for j, c in enumerate(s):
#       if c == "#":
#         if ii == -1:
#           ii = j
#       else:
#         if ii != -1:
#           groups.append(j - ii)
#           ii = -1
#     if ii != -1:
#       groups.append(len(s) - ii)
#     if groups == g:
#       return 1
#     return 0
#   else:
#     for aa in range(a):
#       if s[aa] == "#":
#         if ii == -1:
#           ii = aa
#       else:
#         if ii != -1:
#           if group_num >= len(g) or aa - ii != g[group_num]:
#             return 0
#           group_num += 1
#           ii = -1
#     if ii != -1:
#       if group_num >= len(g) or a - ii > g[group_num]:
#         return 0
#   num = 0
#   if s[a] == "?":
#     num += recur(s[:a] + "#" + s[a + 1:], g, a + 1)
#     num += recur(s[:a] + "." + s[a + 1:], g, a + 1)
#   else:
#     num += recur(s, g, a + 1)
#   return num
