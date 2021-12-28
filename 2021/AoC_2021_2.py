data = open("AoC_2021_2.txt").read().split('\n')
position = depth = depth2 = aim = 0
for i in data:
    direction, num = i.split(" ")
    if direction == 'forward':
        position += int(num)
        depth2 += aim * int(num)
    elif direction == 'up':
        depth -= int(num)
        aim -= int(num)
    else:
        depth += int(num)
        aim += int(num)
print('Part 1: %d; part 2: %d' % (position * depth, position * depth2))
