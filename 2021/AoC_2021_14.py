from collections import defaultdict

data = open('AoC_2021_14.txt').read().split('\n')
template = data[0]
data = data[2:]
# for i in range(10):                                   # old part 1
#     new_template = ''
#     for j in range(0, len(template)):
#         for d in data:
#             s, letter = d.split(' -> ')
#             if template[j:j + 2] == s:
#                 new_template += template[j] + letter
#                 break
#     template = new_template + template[-1]
# min_num = 1000000000000000000000
# max_num = -1
# for i in set(template):
#     if template.count(i) < min_num:
#         min_num = template.count(i)
#     elif template.count(i) > max_num:
#         max_num = template.count(i)
# print(max_num - min_num)
mapping = dict()
for i in data:
    mapping[i.split(' -> ')[0]] = i.split(' -> ')[1]
part1indices = defaultdict(int)
indices = defaultdict(int)
for i in range(len(template) - 1):
    indices[template[i:i + 2]] += 1
for i in range(40):
    temp = indices.copy()
    for j, c in indices.items():
        if c > 0:
            temp[j] -= c
            temp[j[0] + mapping[j]] += c
            temp[mapping[j] + j[1]] += c
    indices = temp
    if i == 9:
        part1indices = indices

part1count = defaultdict(int)
for i, j in part1indices.items():
    part1count[i[0]] += j
    part1count[i[1]] += j

part2count = defaultdict(int)
for i, j in indices.items():
    part2count[i[0]] += j
    part2count[i[1]] += j
print('Part 1: %d; part 2: %s' % ((max(part1count.values()) - min(part1count.values()) - 1) // 2,
                                  (max(part2count.values()) - min(part2count.values()) - 1) // 2))
