from collections import defaultdict

data = open('AoC_2021_22.txt').read().split('\n')
# on = set()                # old part 1
# for i in data:
#     x, y, z = i.split(',')
#     temp_x = x.split('=')[1]
#     x_min, x_max = tuple(map(int, temp_x.split('..')))
#     temp_y = y.split('=')[1]
#     y_min, y_max = tuple(map(int, temp_y.split('..')))
#     temp_z = z.split('=')[1]
#     z_min, z_max = tuple(map(int, temp_z.split('..')))
#     if x_min < -50 and x_max < -50 or x_min > 50 and x_max > 50 or y_min < -50 and y_max < -50 or \
#             y_min > 50 and y_max > 50 or z_min < -50 and z_max < -50 or z_min > 50 and z_max > 50:
#         continue
#     cubes = set()
#     for j in range(x_min, x_max + 1):
#         for k in range(y_min, y_max + 1):
#             for m in range(z_min, z_max + 1):
#                 cubes.add((j, k, m))
#     if i.split()[0] == 'on':
#         on = on.union(cubes)
#     else:
#         on = on.difference(cubes)
# print(len(on))

p1 = defaultdict(int)
on = defaultdict(int)
for i in data:
    (x_min, x_max), (y_min, y_max), (z_min, z_max) = (tuple(map(int, temp.split('..'))) for temp in
                                                      (num.split('=')[1] for num in i.split(',')))
    if not (p1 or all(-50 <= val <= 50 for val in (x_min, x_max, y_min, y_max, z_min, z_max))):
        p1 = on.copy()
    on_temp = on.copy()
    for (x, y, z), count in on.items():
        if (x_min <= x[0] <= x_max or x_min <= x[1] <= x_max or x[0] <= x_min and x_max <= x[1]) and \
                (y_min <= y[0] <= y_max or y_min <= y[1] <= y_max or y[0] <= y_min and y_max <= y[1]) and \
                (z_min <= z[0] <= z_max or z_min <= z[1] <= z_max or z[0] <= z_min and z_max <= z[1]):
            on_temp[(max(x_min, x[0]), min(x_max, x[1])),  # the intersection of two cuboids
                    (max(y_min, y[0]), min(y_max, y[1])),
                    (max(z_min, z[0]), min(z_max, z[1]))] += -count
            # alternating between adding and subtracting off cuboids (above line) to avoid double-counting
    on = on_temp
    on[((x_min, x_max), (y_min, y_max), (z_min, z_max))] += i.split()[0] == 'on'
part1, part2 = (sum([(i[0][1] - i[0][0] + 1) * (i[1][1] - i[1][0] + 1) * (i[2][1] - i[2][0] + 1) * m
                     for i, m in i.items()]) for i in (p1, on))
print('Part 1: %d; part 2: %d' % (part1, part2))
