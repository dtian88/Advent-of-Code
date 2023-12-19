from copy import deepcopy
from math import prod


def find_combos(wf, ranges):
  if wf == "A":
    return prod(end - start + 1 for start, end in ranges.values())
  if wf == "R":
    return 0
  rules = workflows[wf][1:-1].split(",")
  combos = 0
  for rule in rules:
    if ":" in rule:
      cond, next = rule.split(":")
      new_ranges = deepcopy(ranges)
      new_ranges[cond[0]]["><".index(cond[1])] = int(cond[2:]) + (1 if cond[1] == ">" else -1)
      if new_ranges[cond[0]][0] <= new_ranges[cond[0]][1]:
        combos += find_combos(next, new_ranges)
      ranges[cond[0]]["<>".index(cond[1])] = int(cond[2:])
    else:
      combos += find_combos(rule, ranges)
  return combos


w, r = open("AoC_2023_19.txt").read().split("\n\n")
workflows = {line[:line.index("{")]: line[line.index("{"):] for line in w.split("\n")}
part1 = 0

for ratings in r.split("\n"):
  wf = "in"
  r = {rating[0]: int(rating[2:]) for rating in ratings[1:-1].split(",")}
  done = False
  while not done:
    rules = workflows[wf][1:-1].split(",")
    for rule in rules:
      cond, next = rule.split(":") if ":" in rule else ("", rule)
      if not cond or eval("r[\"" + cond[0] + "\"]" + cond[1:]):
        if next in "AR":
          done = True
          if next == "A":
            part1 += sum(r.values())
        else:
          wf = next
        break

print("Part 1: %d; part 2: %d" % (part1, find_combos("in", {v: [1, 4000] for v in "xmas"})))


# def find_combos(wf, ranges):
#   if wf == "A":
#     return prod(map(len, ranges.values()))
#   if wf == "R":
#     return 0
#   rules = w[wf][1:-1].split(",")
#   combos = 0
#   for rule in rules:
#     if ":" in rule:
#       cond, next = rule.split(":")
#       new_ranges = deepcopy(ranges)
#       new_ranges[cond[0]] &= {v for v in range(1, 4001) if eval("v" + cond[1:])}
#       combos += find_combos(next, new_ranges)
#       ranges[cond[0]] &= {v for v in range(1, 4001) if not eval("v" + cond[1:])}
#     else:
#       combos += find_combos(rule, ranges)
#   return combos


# print("Part 1: %d; part 2: %d" % (part1, find_combos_2("in", {v: set(range(1, 4001)) for v in "xmas"})))
