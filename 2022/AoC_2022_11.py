from collections import deque
from math import prod

data = [i.split("\n") for i in open("AoC_2022_11.txt").read().strip().split('\n\n')]
parts = [-1, -1]
for part in range(2):
    monkeys, ops, amt, div, tf = ([] for _ in range(5))
    for lines in data:
        monkeys.append(deque(map(int, lines[1].split(": ")[1].split(", "))))
        ops.append(lines[2].split()[-2])
        amt.append(int(lines[2].split()[-1]) if lines[2].count("old") == 1 else -1)
        div.append(int(lines[3].split()[-1]))
        tf.append((int(lines[5].split()[-1]), int(lines[4].split()[-1])))
    product = prod(div)
    inspected = [0 for _ in range(8)]
    for _ in range(20 if part else 10000):
        for monkey in range(8):
            while monkeys[monkey]:
                inspected[monkey] += 1
                item = monkeys[monkey].popleft()
                a = amt[monkey] if amt[monkey] != -1 else item
                item = item * a if ops[monkey] == "*" else item + a
                item = item // 3 if part else item % product
                monkeys[tf[monkey][item % div[monkey] == 0]].append(item)
    inspected.sort(reverse=True)
    parts[1-part] = inspected[0] * inspected[1]
print('Part 1: %s; part 2: %s' % (parts[0], parts[1]))
