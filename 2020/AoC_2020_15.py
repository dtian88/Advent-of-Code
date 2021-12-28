data, spoken, pt1, current, answer = [2,1,10,11,0,6], {2: 1, 1: 2, 10: 3, 11: 4, 0: 5, 6: 6}, 0, 0, 0
for i in range(7, 30000001):  # part 2
    answer = current
    current = i - spoken[current] if current in spoken else 0
    spoken[answer] = i
    if i == 2020:  # part 1
        pt1 = answer
print('Part 1: %d; part 2: %d' % (pt1, answer))

# for i in range(len(data)):    # old part 1 code that is extremely inefficient and could not solve part 2 quickly
#     spoken[i + 1] = data[i]
# for i in range(7, 2020):
#     if spoken[i - 1] in spoken.values():
#         s = set()
#         for j, val in spoken.items():
#             if val == spoken[i - 1]:
#                 s.add(j)
#         maximum = max(s)
#         s.remove(maximum)
#         spoken[i] = maximum - max(s) if s else 0
#         for j in s:
#             del spoken[j]
#     else:
#         spoken[i] = 0
# print(spoken[2021])

# data, spoken, pt1 = [2, 1, 10, 11, 0, 6], {}, 0   # old part 2 code before I realized lists as values were not needed
# for i in range(len(data)):
#     spoken[data[i]] = [i + 1]
# previous = data[-1]
# for i in range(7, 30000001):  # part 2
#     if len(spoken[previous]) == 1:
#         spoken[0].append(i)
#         previous = 0
#     else:
#         previous = spoken[previous][-1] - spoken[previous][-2]
#         if previous not in spoken:
#             spoken[previous] = []
#         spoken[previous].append(i)
#     if i == 2020:  # part 1
#         pt1 = previous
# print('Part 1: %d; part 2: %d' % (pt1, previous))