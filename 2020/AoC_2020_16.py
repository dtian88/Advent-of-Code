data = open("AoC_2020_16.txt").read().split('\n\n')
rules, valid, valid_2 = data[0].split('\n'), set(), {}          # part 1
for i in rules:
    temp, second_range = i.split(' or ')
    name, first_range = temp.split(': ')
    valid = valid.union(range(int(first_range.split('-')[0]), int(first_range.split('-')[1]) + 1)).union(   # part 1
        range(int(second_range.split('-')[0]), int(second_range.split('-')[1]) + 1))
    valid_2[name] = set(range(int(first_range.split('-')[0]), int(first_range.split('-')[1]) + 1)).union(   # part 2
        range(int(second_range.split('-')[0]), int(second_range.split('-')[1]) + 1))
nearby = data[2].split('\n')[1:]
pt1 = sum(sum([int(j) for j in i.split(',') if int(j) not in valid]) for i in nearby)
invalids = set()        # part 2
for i in nearby:
    for j in i.split(','):
        if int(j) not in valid:
            invalids.add(i)
            break
for invalid in invalids:
    nearby.remove(invalid)
nearby.append(data[1].split('\n')[1])
possibles, nearby_2, fields, pt2 = {}, [[] for i in range(len(nearby))], {}, 1
for i in range(len(nearby)):
    nearby_2[i] = list(map(int, nearby[i].split(',')))
for k, l in valid_2.items():
    for i in range(len(nearby_2[0])):
        ok = True
        for j in range(len(nearby_2)):
            if nearby_2[j][i] not in l:
                ok = False
                break
        if ok:
            if k not in possibles:
                possibles[k] = set()
            possibles[k].add(i)
while len(fields) < len(possibles):
    for name, nums in possibles.items():
        if len(nums) == 1:
            fields[name] = list(nums)[0]
            for name2, nums2 in possibles.items():
                if fields[name] in nums2:
                    nums2.remove(fields[name])
for name, index in fields.items():
    if name.startswith('departure'):
        pt2 *= nearby_2[-1][index]
print('Part 1: %d; part 2: %d' % (pt1, pt2))