data = open("AoC_2023_4.txt").read().split('\n')
part1 = 0
copies = [0 for _ in data]
for idx, card in enumerate(data):
  winning, have = (ii.split(" ") for ii in card.split(": ")[1].split(" | "))
  if count := sum([h != "" and h in winning for h in have]):
    part1 += 2 ** (count - 1)
    if idx != len(data) - 1:
      while count > 0:
        for d in range(idx + 1, len(data)):
          copies[d] += 1 + copies[idx]
          if (count := count - 1) == 0:
            break

print('Part 1: %d; part 2: %d' % (part1, sum(copies) + len(data)))
