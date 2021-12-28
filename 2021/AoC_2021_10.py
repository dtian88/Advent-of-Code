data = open('AoC_2021_10.txt').read().split('\n')
count = 0
removed = []
for i in data:
    j = i
    stack = [i[0]]
    i = i[1:]
    while stack and i:
        if i[0] in (')', ']', '>', '}'):
            char = stack.pop()
            if i[0] == ')' and not char == '(':
                count += 3
                removed.append(j)
                break
            elif i[0] == ']' and not char == '[':
                count += 57
                removed.append(j)
                break
            elif i[0] == '}' and not char == '{':
                count += 1197
                removed.append(j)
                break
            elif i[0] == '>' and not char == '<':
                count += 25137
                removed.append(j)
                break
        else:
            stack.append(i[0])
        i = i[1:]

counts = []
for i in removed:
    data.remove(i)
for i in data:
    j = i
    stack = [i[0]]
    i = i[1:]
    while stack and i:
        if i[0] in (')', ']', '>', '}'):
            stack.pop()
        else:
            stack.append(i[0])
        i = i[1:]
    s = 0
    stack.reverse()
    for j in stack:
        s *= 5
        s += ['(', '[', '{', '<'].index(j) + 1 if j in ['(', '[', '{', '<'] else 0
    counts.append(s)
counts.sort()
print('Part 1: %d; part 2: %d' % (count, counts[len(counts) // 2]))
