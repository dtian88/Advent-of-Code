from collections import defaultdict

data = open("AoC_2022_7.txt").read().strip().split('\n')
part1, part2 = 0, float('inf')
child = defaultdict(set)  # parent: { children }
parent = {}  # child: parent
num_files, files_in_dir = defaultdict(int), defaultdict(set)
current, seen, path = "", set(), []
ls = False
for i in data:
    if i.split()[0] == "$":
        if ls:
            ls = False
            if current not in seen:
                seen.add(current)
                temp = current
                tempval = num_files[temp]
                while temp != '/':
                    temp = parent[temp]
                    num_files[temp] += tempval
        if i.split()[1] == "cd":
            if i.split()[2] == "..":
                path.pop()
                current = parent[current]
            else:
                path.append(i.split()[2])
                current = ",".join(path)
        elif i.split()[1] == "ls":
            ls = True
    elif i.split()[0] == "dir":
        parent[current + "," + i.split()[1]] = current
        child[current].add(current + "," + i.split()[1])
    elif current + "," + i.split()[1] not in files_in_dir[current]:
        files_in_dir[current].add(current + "," + i.split()[1])
        num_files[current] += int(i.split()[0])
if ls and current not in seen:
    temp = current
    tempval = num_files[temp]
    while temp != '/':
        temp = parent[temp]
        num_files[temp] += tempval

for i, v in num_files.items():
    if v <= 100000:
        part1 += v
    if 70000000 - (num_files['/'] - v) >= 30000000 and v < part2:
        part2 = v
print('Part 1: %s; part 2: %s' % (part1, part2))
