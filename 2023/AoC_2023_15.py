from collections import OrderedDict

def hash_algorithm(s):
  h = 0
  for c in s:
    h = 17 * (h + ord(c)) % 256
  return h


data = open("AoC_2023_15.txt").read().split(",")
part1 = part2 = 0
boxes = [OrderedDict() for _ in range(256)]

for step in data:
  part1 += hash_algorithm(step)
  label = step[:-1 if step[-1] == "-" else -2]
  h = hash_algorithm(label)
  if step[-1] == "-":
    boxes[h].pop(label, None)
  else:
    boxes[h][label] = int(step[-1])

for box_num, box in enumerate(boxes):
  for slot_num, focal_length in enumerate(box.values()):
    part2 += (box_num + 1) * (slot_num + 1) * focal_length
  
print("Part 1: %d; part 2: %d" % (part1, part2))
