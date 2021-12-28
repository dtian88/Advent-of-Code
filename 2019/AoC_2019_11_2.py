from collections import deque
data = [3,8,1005,8,310,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,29,1,2,11,10,1,1101,2,10,2,1008,18,10,2,106,3,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,67,2,105,15,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,93,2,1001,16,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,119,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,141,2,7,17,10,1,1103,16,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,170,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,193,1,7,15,10,2,105,13,10,1006,0,92,1006,0,99,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,228,1,3,11,10,1006,0,14,1006,0,71,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,261,2,2,2,10,1006,0,4,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,289,101,1,9,9,1007,9,1049,10,1005,10,15,99,109,632,104,0,104,1,21101,0,387240009756,1,21101,327,0,0,1105,1,431,21101,0,387239486208,1,21102,1,338,0,1106,0,431,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,3224472579,1,1,21101,0,385,0,1106,0,431,21101,0,206253952003,1,21102,396,1,0,1105,1,431,3,10,104,0,104,0,3,10,104,0,104,0,21102,709052072296,1,1,21102,419,1,0,1105,1,431,21102,1,709051962212,1,21102,430,1,0,1106,0,431,99,109,2,21202,-1,1,1,21102,1,40,2,21102,462,1,3,21102,452,1,0,1105,1,495,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,457,458,473,4,0,1001,457,1,457,108,4,457,10,1006,10,489,1101,0,0,457,109,-2,2105,1,0,0,109,4,2102,1,-1,494,1207,-3,0,10,1006,10,512,21101,0,0,-3,22101,0,-3,1,21202,-2,1,2,21102,1,1,3,21101,531,0,0,1105,1,536,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,559,2207,-4,-2,10,1006,10,559,21202,-4,1,-4,1105,1,627,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,578,0,1105,1,536,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,597,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,619,21201,-1,0,1,21102,1,619,0,106,0,494,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

for i in range(100000):
  data.append(0)

relative_base = 0

first = True
curr = 200 * 10 + 100
painted = set()
grid = ' ' * 20 * 200
angle = 0
angle_dict = {0: -200, 1: 1, 2: 200, 3: -1} #0 up, 1 right, 2 down, 3 left
color = 0

i = 0
while i < len(data):
  if data[i] == 1:
    data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
    i += 4
  elif data[i] == 2:
    data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
    i += 4
  elif data[i] == 3:
    if grid[curr] == '.':
      data[data[i + 1]] = 0
    else:
      data[data[i + 1]] = 1
    i += 2
  elif data[i] == 4:
    if first:
      color = data[data[i + 1]]
      first = False
      if color:
        grid = grid[:curr] + '#' + grid[curr + 1:]
      else:
        grid = grid[:curr] + ' ' + grid[curr + 1:]
    else:
      temp = data[data[i + 1]]
      if temp:
        angle += 1
      else:
        angle -= 1
      if angle > 3:
        angle -= 4
      elif angle < 0:
        angle += 4
      painted.add(curr)
      curr += angle_dict[angle]
      first = True
    i += 2
  elif data[i] == 5:
    if data[data[i + 1]] != 0:
      i = data[data[i + 2]]
    else:
      i += 3
  elif data[i] == 6:
    if data[data[i + 1]] == 0:
      i = data[data[i + 2]]
    else:
      i += 3
  elif data[i] == 7:
    if data[data[i + 1]] < data[data[i + 2]]:
      data[data[i + 3]] = 1
    else:
      data[data[i + 3]] = 0
    i += 4
  elif data[i] == 8:
    if data[data[i + 1]] == data[data[i + 2]]:
      data[data[i + 3]] = 1
    else:
      data[data[i + 3]] = 0
    i += 4
  elif data[i] == 9:
    relative_base += data[data[i + 1]]
    i += 2
  elif data[i] == 99:
    break
  else:
    opcode = int(str(data[i])[:-3:-1][::-1])
    if opcode == 1 or opcode == 2:
      one = 0
      two = 0
      three = 0
      if len(str(data[i])) > 4:
        three = int(str(data[i])[-5])
      if len(str(data[i])) > 3:
        two = int(str(data[i])[-4])
      if len(str(data[i])) > 2:
        one = int(str(data[i])[-3])
      num_one = 0
      num_two = 0
      num_three = 0
      if one == 0:
        num_one = data[data[i + 1]]
      elif one == 1:
        num_one = data[i + 1]
      else:
        num_one = data[relative_base + data[i + 1]]
      if two == 0:
        num_two = data[data[i + 2]]
      elif two == 1:
        num_two = data[i + 2]
      else:
        num_two = data[relative_base + data[i + 2]]
      if three == 0:
        num_three = data[i + 3]
      else:
        num_three = relative_base + data[i + 3]
      if opcode == 1:
        result = num_one + num_two
      elif opcode == 2:
        result = num_one * num_two
      data[num_three] = result
      i += 4
    elif opcode == 3 or opcode == 4:
      one = 0
      if len(str(data[i])) > 2:
        one = int(str(data[i])[-3])
      num_one = 0
      if one == 0 or one == 1:
        num_one = data[i + 1]
      else:
        num_one = relative_base + data[i + 1]
      if opcode == 3:
        if grid[curr] == '.':
          data[num_one] = 0
        else:
          data[num_one] = 1
      elif opcode == 4:
        if first:
          if one == 1:
            color = num_one
          else:
            color = data[num_one]
          first = False
          if color:
            grid = grid[:curr] + '#' + grid[curr + 1:]
          else:
            grid = grid[:curr] + ' ' + grid[curr + 1:]
        else:
          if one == 1:
            temp = num_one
          else:
            temp = data[num_one]
          if temp:
            angle += 1
          else:
            angle -= 1
          if angle > 3:
            angle -= 4
          elif angle < 0:
            angle += 4
          painted.add(curr)
          curr += angle_dict[angle]
          first = True
      i += 2
    elif opcode == 5 or opcode == 6:
      one = 0
      two = 0
      if len(str(data[i])) > 3:
        two = int(str(data[i])[-4])
      if len(str(data[i])) > 2:
        one = int(str(data[i])[-3])
      num_one = 0
      num_two = 0
      if one == 0:
        num_one = data[data[i + 1]]
      elif one == 1:
        num_one = data[i + 1]
      else:
        num_one = data[relative_base + data[i + 1]]
      if two == 0:
        num_two = data[data[i + 2]]
      elif two == 1:
        num_two = data[i + 2]
      else:
        num_two = data[relative_base + data[i + 2]]
      if opcode == 5:
        if num_one != 0:
          i = num_two
        else:
          i += 3
      elif opcode == 6:
        if num_one == 0:
          i = num_two
        else:
          i += 3
    elif opcode == 7 or opcode == 8:
      one = 0
      two = 0
      three = 0
      if len(str(data[i])) > 4:
        three = int(str(data[i])[-5])
      if len(str(data[i])) > 3:
        two = int(str(data[i])[-4])
      if len(str(data[i])) > 2:
        one = int(str(data[i])[-3])
      num_one = 0
      num_two = 0
      num_three = 0
      if one == 0:
        num_one = data[data[i + 1]]
      elif one == 1:
        num_one = data[i + 1]
      else:
        num_one = data[relative_base + data[i + 1]]
      if two == 0:
        num_two = data[data[i + 2]]
      elif two == 1:
        num_two = data[i + 2]
      else:
        num_two = data[relative_base + data[i + 2]]
      if three == 0:
        num_three = data[i + 3]
      else:
        num_three = relative_base + data[i + 3]
      if opcode == 7:
        if num_one < num_two:
          data[num_three] = 1
        else:
          data[num_three] = 0
      elif opcode == 8:
        if num_one == num_two:
          data[num_three] = 1
        else:
          data[num_three] = 0
      i += 4
    elif opcode == 9:
      one = 0
      if len(str(data[i])) > 2:
        one = int(str(data[i])[-3])
      num_one = 0
      if one == 0:
        num_one = data[data[i + 1]]
      elif one == 1:
        num_one = data[i + 1]
      else:
        num_one = data[relative_base + data[i + 1]]
      relative_base += num_one
      i += 2
    else:
      i += 1
    
for i in range(20):
  temp_index = grid[i * 200:i * 200 + 200].find('#') - 101
  temp = grid[i * 200:i * 200 + 200].strip(' ')
  if temp:
    print(' ' * temp_index + temp)