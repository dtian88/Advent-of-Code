data = open("AoC_2020_17.txt").read().split('\n')
active, inactive, active2, inactive2 = set(), set(), set(), set()  # part 1
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            active.add((i, j, 0))
            active2.add((i, j, 0, 0))
        else:
            inactive.add((i, j, 0))
            inactive2.add((i, j, 0, 0))
for i in range(6):
    inactivated = set()
    for c in active:
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if (dx, dy, dz) != (0, 0, 0):
                        if (c[0] + dx, c[1] + dy, c[2] + dz) not in active:
                            inactive.add((c[0] + dx, c[1] + dy, c[2] + dz))
                        else:
                            count += 1
        if count != 2 and count != 3:
            inactivated.add(c)
    temp_active, temp_inactive = active.copy().difference(inactivated), inactive.copy().union(inactivated)
    for c in inactive:
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if (dx, dy, dz) != (0, 0, 0) and (c[0] + dx, c[1] + dy, c[2] + dz) in active:
                        count += 1
        if count == 3:
            temp_active.add(c); temp_inactive.remove(c)
    active, inactive = temp_active, temp_inactive
for i in range(6):  # part 2
    inactivated = set()
    for c in active2:
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if (dx, dy, dz, dw) != (0, 0, 0, 0):
                            if (c[0] + dx, c[1] + dy, c[2] + dz, c[3] + dw) not in active2:
                                inactive2.add((c[0] + dx, c[1] + dy, c[2] + dz, c[3] + dw))
                            else:
                                count += 1
        if count != 2 and count != 3:
            inactivated.add(c)
    temp_active, temp_inactive = active2.copy().difference(inactivated), inactive2.copy().union(inactivated)
    for c in inactive2:
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if (dx, dy, dz, dw) != (0, 0, 0, 0) and (c[0] + dx, c[1] + dy, c[2] + dz, c[3] + dw) in active2:
                            count += 1
        if count == 3:
            temp_active.add(c); temp_inactive.remove(c)
    active2, inactive2 = temp_active, temp_inactive
print('Part 1: %d; part 2: %d' % (len(active), len(active2)))
