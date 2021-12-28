add_x = [13, 11, 14, -5, 14, 10, 12, -14, -8, 13, 0, -5, -9, -1]
add_y = [0, 3, 8, 5, 13, 9, 6, 1, 1, 2, 7, 5, 8, 15]
divs = [1, 1, 1, 26, 1, 1, 1, 26, 26, 1, 26, 26, 26, 26]


def recur(place, z, nums, part):
    if place == 14:
        if z == 0:
            globals()[part] = nums
            globals()[part + 'done'] = True
    else:
        for i in ranges[part]:
            equal = z % 26 + add_x[place] == i
            new_z = z // divs[place] * (1 if equal else 26) + (0 if equal else i + add_y[place])
            if not (globals()[part] or (add_x[place] <= 0 and new_z > z // 26)):
                recur(place + 1, new_z, nums + 10 ** (13 - place) * i, part)


part1done = part2done = False
part1 = part2 = 0
ranges = {'part1': range(9, 0, -1), 'part2': range(1, 10)}
recur(0, 0, 0, 'part1')
recur(0, 0, 0, 'part2')
print('Part 1: %d; part 2: %d' % (part1, part2))
