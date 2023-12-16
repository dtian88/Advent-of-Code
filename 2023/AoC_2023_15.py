def hash_algorithm(s):
  h = 0
  for c in s:
    h = 17 * (h + ord(c)) % 256
  return h


data = open("AoC_2023_15.txt").read().split(",")
part1 = 0
boxes = [{} for _ in range(256)]

for step in data:
  part1 += hash_algorithm(step)
  label = step[:-1 if step[-1] == "-" else -2]
  num = hash_algorithm(label)
  if step[-1] == "-":
    boxes[num].pop(label, None)
  else:
    boxes[num][label] = int(step[-1])

print("Part 1: %d; part 2: %d" % (part1, sum(sum((num + 1) * (slot + 1) * focal_length for slot, focal_length in enumerate(box.values())) for num, box in enumerate(boxes))))
