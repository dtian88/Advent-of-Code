data = open('AoC_2021_8.txt').read().split('\n')
count = 0
data2 = [i.split(' | ') for i in data]
for i, o in data2:
    wiring = dict()
    for j in i.split():
        s = set(j)
        if len(s) == 2:
            wiring[1] = s
        elif len(s) == 3:
            wiring[7] = s
        elif len(s) == 4:
            wiring[4] = s
        elif len(s) == 7:
            wiring[8] = s
    for j in i.split():
        s = set(j)
        if len(wiring[8].intersection(s)) == 6 and len(wiring[4].intersection(s)) == 4:  # 1, 4, 7, 8, 9
            wiring[9] = s
    for j in i.split():
        s = set(j)
        if len(s) == 5:
            if len(wiring[9].intersection(s)) == 4:
                wiring[2] = s
            else:
                if len(wiring[1].intersection(s)) == 1:
                    wiring[5] = s
                else:
                    wiring[3] = s  # 1, 2, 3, 4, 5, 7, 8, 9    0, 6 left
    for j in i.split():
        s = set(j)
        if s not in wiring.values():
            if len(wiring[1].intersection(s)) == 1:
                wiring[6] = s
            else:
                wiring[0] = s
    split = o.split()
    count += sum(
        [sum([c * 10 ** (3 - j) if d == set(split[j]) else 0 for c, d in wiring.items()]) for j in range(len(split))])
print('Part 1: %d; part 2: %d' % (
    sum([sum([len(set(j)) in (2, 3, 4, 7) for j in i.split()]) for i in [k.split(' | ')[1] for k in data]]), count))
