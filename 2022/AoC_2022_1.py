data = open("AoC_2022_1.txt").read().split('\n')
s = s1 = s2 = temp = 0
for i in data:
    if not i:
        if temp > s:
            s2 = s1
            s1 = s
            s = temp
        elif temp > s1:
            s2 = s1
            s1 = temp
        else:
            s2 = max(s2, temp)
        temp = 0
    else:
        temp += int(i)
print('Part 1: %d; part 2: %d' % (s, s + s1 + s2))

# data = open("AoC_2022_1.txt").read().split('\n\n')
# s = sorted([sum(list(map(int, i.split('\n')))) for i in data], reverse=True)
# print('Part 1: %d; part 2: %d' % (s[0], sum(s[:3])))
