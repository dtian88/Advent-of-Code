from functools import cmp_to_key

data = [i.split() for i in open("AoC_2023_7.txt").read().split('\n')]
values = ["A", "K", "Q", "J", "T", *[str(i) for i in range(9, 1, -1)]]
values2 = ["A", "K", "Q", "T", *[str(i) for i in range(9, 1, -1)], "J"]

def hand_type(hand, part, values):
  num_j = 0
  counts = {v: 0 for v in values}
  for card in hand:
    if part != 2 or card != "J":
      counts[card] += 1
    else:
      num_j += 1
  if part == 2:
    highest_val = max(counts, key=counts.get)
    if counts[highest_val] > 0:
      counts[highest_val] += num_j
      highest = counts[highest_val]
    else:
      highest = 5
  else:
    highest = max(counts.values())
  if highest == 5 or highest == 4:
    return 5 - highest
  if highest == 3:
    if 2 in counts.values():
      return 2
    return 3
  if highest == 2:
    if list(counts.values()).count(2) == 2:
      return 4
    return 5
  return 6


def compare(hand1, hand2, part, values):
  if (type1 := hand_type(hand1, part, values)) != (type2 := hand_type(hand2, part, values)):
    return type1 - type2
  for i in range(len(hand1)):
    if (val1 := values.index(hand1[i])) != (val2 := values.index(hand2[i])):
      return val1 - val2
  return 0

print('Part 1: %d; part 2: %d' % (
  sum((i + 1) * int(val) for i, (_, val) in enumerate(sorted(data, key=cmp_to_key(lambda line1, line2: compare(line2[0], line1[0], 1, values))))),
  sum((i + 1) * int(val) for i, (_, val) in enumerate(sorted(data, key=cmp_to_key(lambda line1, line2: compare(line2[0], line1[0], 2, values2)))))))
