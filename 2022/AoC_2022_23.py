# 69/180
data = open("AoC_2022_23.txt").read().split('\n')
elves = {(i, j) for i, line in enumerate(data) for j, c in enumerate(line) if c == '#'}
x = part1 = 0
while True:
    new_pos = dict()
    conflicts = set()
    for elf in elves:
        north_blocked = any(
            i in elves for i in ((elf[0] - 1, elf[1]), (elf[0] - 1, elf[1] - 1), (elf[0] - 1, elf[1] + 1)))
        south_blocked = any(
            i in elves for i in ((elf[0] + 1, elf[1]), (elf[0] + 1, elf[1] - 1), (elf[0] + 1, elf[1] + 1)))
        west_blocked = any(
            i in elves for i in ((elf[0], elf[1] - 1), (elf[0] - 1, elf[1] - 1), (elf[0] + 1, elf[1] - 1)))
        east_blocked = any(
            i in elves for i in ((elf[0], elf[1] + 1), (elf[0] - 1, elf[1] + 1), (elf[0] + 1, elf[1] + 1)))
        if not(north_blocked or south_blocked or west_blocked or east_blocked):
            new_pos[elf] = elf
            continue
        if x % 4 == 0:
            if not north_blocked:
                if (elf[0] - 1, elf[1]) in new_pos.values():
                    conflicts.add((elf[0] - 1, elf[1]))
                new_pos[elf] = (elf[0] - 1, elf[1])
            elif not south_blocked:
                if (elf[0] + 1, elf[1]) in new_pos.values():
                    conflicts.add((elf[0] + 1, elf[1]))
                new_pos[elf] = (elf[0] + 1, elf[1])
            elif not west_blocked:
                if (elf[0], elf[1] - 1) in new_pos.values():
                    conflicts.add((elf[0], elf[1] - 1))
                new_pos[elf] = (elf[0], elf[1] - 1)
            elif not east_blocked:
                if (elf[0], elf[1] + 1) in new_pos.values():
                    conflicts.add((elf[0], elf[1] + 1))
                new_pos[elf] = (elf[0], elf[1] + 1)
            else:
                new_pos[elf] = elf
        elif x % 4 == 1:
            if not south_blocked:
                if (elf[0] + 1, elf[1]) in new_pos.values():
                    conflicts.add((elf[0] + 1, elf[1]))
                new_pos[elf] = (elf[0] + 1, elf[1])
            elif not west_blocked:
                if (elf[0], elf[1] - 1) in new_pos.values():
                    conflicts.add((elf[0], elf[1] - 1))
                new_pos[elf] = (elf[0], elf[1] - 1)
            elif not east_blocked:
                if (elf[0], elf[1] + 1) in new_pos.values():
                    conflicts.add((elf[0], elf[1] + 1))
                new_pos[elf] = (elf[0], elf[1] + 1)
            elif not north_blocked:
                if (elf[0] - 1, elf[1]) in new_pos.values():
                    conflicts.add((elf[0] - 1, elf[1]))
                new_pos[elf] = (elf[0] - 1, elf[1])
            else:
                new_pos[elf] = elf
        elif x % 4 == 2:
            if not west_blocked:
                if (elf[0], elf[1] - 1) in new_pos.values():
                    conflicts.add((elf[0], elf[1] - 1))
                new_pos[elf] = (elf[0], elf[1] - 1)
            elif not east_blocked:
                if (elf[0], elf[1] + 1) in new_pos.values():
                    conflicts.add((elf[0], elf[1] + 1))
                new_pos[elf] = (elf[0], elf[1] + 1)
            elif not north_blocked:
                if (elf[0] - 1, elf[1]) in new_pos.values():
                    conflicts.add((elf[0] - 1, elf[1]))
                new_pos[elf] = (elf[0] - 1, elf[1])
            elif not south_blocked:
                if (elf[0] + 1, elf[1]) in new_pos.values():
                    conflicts.add((elf[0] + 1, elf[1]))
                new_pos[elf] = (elf[0] + 1, elf[1])
            else:
                new_pos[elf] = elf
        else:
            if not east_blocked:
                if (elf[0], elf[1] + 1) in new_pos.values():
                    conflicts.add((elf[0], elf[1] + 1))
                new_pos[elf] = (elf[0], elf[1] + 1)
            elif not north_blocked:
                if (elf[0] - 1, elf[1]) in new_pos.values():
                    conflicts.add((elf[0] - 1, elf[1]))
                new_pos[elf] = (elf[0] - 1, elf[1])
            elif not south_blocked:
                if (elf[0] + 1, elf[1]) in new_pos.values():
                    conflicts.add((elf[0] + 1, elf[1]))
                new_pos[elf] = (elf[0] + 1, elf[1])
            elif not west_blocked:
                if (elf[0], elf[1] - 1) in new_pos.values():
                    conflicts.add((elf[0], elf[1] - 1))
                new_pos[elf] = (elf[0], elf[1] - 1)
            else:
                new_pos[elf] = elf
    new_elves = {old if new in conflicts else new for old, new in new_pos.items()}
    if x == 9:
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')
        for i, j in new_elves:
            min_x, max_x, min_y, max_y = min(min_x, i), max(max_x, i), min(min_y, j), max(max_y, j)
        part1 = (max_x - min_x + 1) * (max_y - min_y + 1) - sum(
            (min_x <= i <= max_x and min_y <= j <= max_y for i, j in new_elves))
    if elves == new_elves:
        print('Part 1: %d; part 2: %d' % (part1, x + 1))
        break
    elves = new_elves
    x += 1
