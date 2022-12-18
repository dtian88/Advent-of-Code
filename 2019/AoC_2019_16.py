import numpy as np

data = '59791871295565763701016897619826042828489762561088671462844257824181773959378451545496856546977738269316476252007337723213764111739273853838263490797537518598068506295920453784323102711076199873965167380615581655722603274071905196479183784242751952907811639233611953974790911995969892452680719302157414006993581489851373437232026983879051072177169134936382717591977532100847960279215345839529957631823999672462823375150436036034669895698554251454360619461187935247975515899240563842707592332912229870540467459067349550810656761293464130493621641378182308112022182608407992098591711589507803865093164025433086372658152474941776320203179747991102193608'
# for i in range(100):
#   print(i)
#   new = ''
#   for j in range(len(data)):
#     num = 0
#     count = 1
#     pattern = []
#     for a in range(j + 1):
#       pattern.append(0)
#     for a in range(j + 1):
#       pattern.append(1)
#     for a in range(j + 1):
#       pattern.append(0)
#     for a in range(j + 1):
#       pattern.append(-1)
#     for k in range(len(data)):
#       num += pattern[count] * int(data[k])
#       count += 1
#       if count == len(pattern):
#         count = 0
#     new += str(num)[-1]
#   data = new
#
# print(data[:8])

data = np.array(list(map(int, [i for i in data])))
base_pattern, patterns = (0, 1, 0, -1), []
for i in range(1, len(data) + 1):
    pattern = []
    j = k = 0
    while len(pattern) <= len(data):
        pattern.append(base_pattern[j % 4])
        k = (k + 1) % i
        if k == 0:
            j += 1
    patterns.append(pattern)
for _ in range(100):
    data = np.array([abs(sum(data * patterns[i][1:])) % 10 for i in range(len(data))])
print(''.join(map(str, data[:8])))
# print()
# data = np.array(list(map(int, [i for i in data])))
# data = np.append(data, data)
# base_pattern, patterns = [0, 1, 0, -1], []
# for i in range(1, len(data) + 1):
#     pattern = []
#     j = k = 0
#     while len(pattern) <= len(data):
#         pattern.append(base_pattern[j % 4])
#         k = (k + 1) % i
#         if k == 0:
#             j += 1
#     patterns.append(pattern)
# for phase in range(10):
#     new_data = np.array([0 for _ in range(len(data))])
#     for i in range(1, len(data) + 1):
#         res = abs(sum(data * patterns[i - 1][1:])) % 10
#         new_data[i - 1] = res
#     data = new_data
#     print(''.join(map(str, data[:8])))
# # print(''.join(map(str, data[:8])))
