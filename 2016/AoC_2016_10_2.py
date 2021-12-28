from collections import deque
with open('data', 'r') as f:
  content = f.readlines()
  content = [x.strip() for x in content]
dictionary = dict()
for l in content:
  if 'value' in l:
    a = l.split(' goes to bot ')
    if int(a[1]) not in dictionary:
      dictionary[int(a[1])] = [int(a[0][6:])]
    else:
      dictionary[int(a[1])].append(int(a[0][6:]))

dictionary2 = dict()
for l in content:
  if 'gives' in l:
    l = l[4:]
    name = l[:l.find(' ')]
    l = l[len(name) + 1:]
    z = l.split('and')
    low = z[0][13:].split(' ')
    high = z[1][8:].split(' ')
    name = int(name)
    if low[0] == 'output':
      dictionary2[name] = [(int(low[1]), 'o')]
    else:
      dictionary2[name] = [(int(low[1]), 'b')]
    if high[1] == 'output':
      dictionary2[name].append((int(high[2]), 'o'))
    else:
      dictionary2[name].append((int(high[2]), 'b'))
output = dict()
one = -1
two = -1
bot = -1
todo = deque()
todo.append(164)

while True:
  bot = todo.popleft()
  one = dictionary[bot][0]
  two = dictionary[bot][1]
  if one > two:
    temp_one = one
    one = two
    two = temp_one
  if dictionary2[bot][0][1] == 'o':
    output[dictionary2[bot][0][0]] = one
  else:
    if dictionary2[bot][0][0] in dictionary:
      dictionary[dictionary2[bot][0][0]].append(one)
      todo.append(dictionary2[bot][0][0])
    else:
      dictionary[dictionary2[bot][0][0]] = [one]
  if dictionary2[bot][1][1] == 'o':
    output[dictionary2[bot][1][0]] = two
  else:
    if dictionary2[bot][1][0] in dictionary:
      dictionary[dictionary2[bot][1][0]].append(two)
      todo.append(dictionary2[bot][1][0])
    else:
      dictionary[dictionary2[bot][1][0]] = [two]
  if dictionary2[bot][0][1] == 'o' and dictionary2[bot][1][1] == 'o':
    break

print(output[0] * output[1] * output[2])