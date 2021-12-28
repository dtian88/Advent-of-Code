from collections import deque, defaultdict
data = open('AoC_2021_12.txt').read().split('\n')
count = count2 = 0
graph = defaultdict(set)
for i in data:
    start, end = i.split('-')
    graph[start].add(end)
    graph[end].add(start)

path = ['start']
queue = deque([path])
while queue:
    n = queue.pop()
    if n[-1] == 'end':
        count += 1
    for b in graph[n[-1]]:
        if not (b[0].islower() and b in n):
            new_path = n.copy()
            new_path.append(b)
            queue.append(new_path)

path = ['start']
queue = deque([(path, False)])
while queue:
    n, twice = queue.pop()
    if n[-1] == 'end':
        count2 += 1
        continue
    for b in graph[n[-1]]:
        num = n.count(b)
        if not (b[0].islower() and (num >= 2 and not twice or num >= 1 and twice)) and not b == 'start':
            new_path = n.copy()
            new_path.append(b)
            if num == 1 and b[0].islower() or twice:
                queue.append((new_path, True))
            else:
                queue.append((new_path, False))
print('Part 1: %d; part 2: %d' % (count, count2))
