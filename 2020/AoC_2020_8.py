data = open("AoC_2020_8.txt").read().split('\n')
acc_1 = acc_2 = accumulator = 0
visited = set()
i = 0
while True:     # part 1
    if i in visited:
        acc_1 = accumulator
        break
    visited.add(i)
    j = data[i].split()
    if j[0] == 'acc':
        accumulator += int(j[1])
    elif j[0] == 'jmp':
        i += int(j[1])
        continue
    i += 1

for a in range(len(data)):      # part 2
    temp = data[a]
    if data[a].startswith('jmp'):
        data[a] = data[a].replace('jmp', 'nop')
    elif data[a].startswith('nop'):
        data[a] = data[a].replace('nop', 'jmp')
    else:
        continue
    visited = set()
    i = accumulator = 0
    while True:     # part 1
        if i in visited:
            break
        visited.add(i)
        if data[i].startswith('acc'):
            accumulator += int(data[i].split()[1])
        elif data[i].startswith('jmp'):
            i += int(data[i].split()[1])
            continue
        i += 1
        if i == len(data) - 1:
            acc_2 = accumulator
            break
    data[a] = temp
print('Part 1: %d; part 2: %d' % (acc_1, acc_2))