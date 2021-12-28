from collections import deque
data = [3,8,1001,8,10,8,105,1,0,0,21,30,51,76,101,118,199,280,361,442,99999,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1002,9,3,9,1001,9,4,9,102,5,9,9,101,3,9,9,1002,9,3,9,4,9,99,3,9,101,5,9,9,102,4,9,9,1001,9,3,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]
num = 0
maximum = -1000000

def reset():
  global data
  data = [3,8,1001,8,10,8,105,1,0,0,21,30,51,76,101,118,199,280,361,442,99999,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1002,9,3,9,1001,9,4,9,102,5,9,9,101,3,9,9,1002,9,3,9,4,9,99,3,9,101,5,9,9,102,4,9,9,1001,9,3,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]

def calculate(input_num):
  i = 0
  while i < len(data):
    if data[i] == 1:
      data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
      i += 4
    elif data[i] == 2:
      data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
      i += 4
    elif data[i] == 3:
      data[data[i + 1]] = input_num.popleft()
      i += 2
    elif data[i] == 4:
      input_num.append(data[data[i + 1]])
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
    elif data[i] == 99:
      break
    else:
      opcode = int(str(data[i])[:-3:-1][::-1])
      if opcode == 1 or opcode == 2:
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
        else:
          num_one = data[i + 1]
        if two == 0:
          num_two = data[data[i + 2]]
        else:
          num_two = data[i + 2]
        if opcode == 1:
          result = num_one + num_two
        elif opcode == 2:
          result = num_one * num_two
        data[data[i + 3]] = result
        i += 4
      elif opcode == 3 or opcode == 4:
        one = 0
        if len(str(data[i])) > 2:
          one = int(str(data[i])[-3])
        num_one = 0
        if one == 0:
          num_one = data[data[i + 1]]
        else:
          num_one = data[i + 1]
        if opcode == 3:
          data[num_one] = input_num.popleft()
        elif opcode == 4:
          input_num.append(num_one)
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
        else:
          num_one = data[i + 1]
        if two == 0:
          num_two = data[data[i + 2]]
        else:
          num_two = data[i + 2]
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
        if len(str(data[i])) > 3:
          two = int(str(data[i])[-4])
        if len(str(data[i])) > 2:
          one = int(str(data[i])[-3])
        num_one = 0
        num_two = 0
        if one == 0:
          num_one = data[data[i + 1]]
        else:
          num_one = data[i + 1]
        if two == 0:
          num_two = data[data[i + 2]]
        else:
          num_two = data[i + 2]
        if opcode == 7:
          if num_one < num_two:
            data[data[i + 3]] = 1
          else:
            data[data[i + 3]] = 0
        elif opcode == 8:
          if num_one == num_two:
            data[data[i + 3]] = 1
          else:
            data[data[i + 3]] = 0
        i += 4
      else:
        i += 1
  return input_num.popleft()

for a in range(5):
  for b in range(5):
    for c in range(5):
      for d in range(5):
        for e in range(5):
          if len(set([a, b, c, d, e])) == 5:
            num = 0
            reset()
            result = 0
            for phase in [a, b, c, d, e]:
              result = calculate(deque([phase, result]))
            if result > maximum:
              maximum = result

print(maximum)