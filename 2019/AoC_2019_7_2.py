from collections import deque
global_data = [3,8,1001,8,10,8,105,1,0,0,21,30,51,76,101,118,199,280,361,442,99999,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1002,9,3,9,1001,9,4,9,102,5,9,9,101,3,9,9,1002,9,3,9,4,9,99,3,9,101,5,9,9,102,4,9,9,1001,9,3,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
queue1 = deque([])
queue2 = deque([])
queue3 = deque([])
queue4 = deque([])
queue5 = deque([])
i1 = i2 = i3 = i4 = i5 = 0
maximum = -1000000, (-1, -1)
def reset():
  global global_data, data1, data2, data3, data4, data5, i1, i2, i3, i4, i5
  data1 = global_data.copy()
  data2 = global_data.copy()
  data3 = global_data.copy()
  data4 = global_data.copy()
  data5 = global_data.copy()
  queue1.clear()
  queue2.clear()
  queue3.clear()
  queue4.clear()
  queue5.clear()
  i1 = i2 = i3 = i4 = i5 = 0

def calculate(input_num, data, i):
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
      return data[data[i + 1]], '4', i
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
      return input_num.popleft(), 99, 0
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
          # if input_num:
          data[num_one] = input_num.popleft()
          # else:
          #   return '3', i
        elif opcode == 4:
          # input_num.append(num_one)
          return num_one, '4', i
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

for a in range(5, 10):
  for b in range(5, 10):
    for c in range(5, 10):
      for d in range(5, 10):
        for e in range(5, 10):
          if len(set([a, b, c, d, e])) == 5:
            reset()
            result = 0
            first = True
            code = -1
            phase = a
            phase_dict = {a:b, b:c, c:d, d:e, e:a}
            deque_dict = {a:queue1, b:queue2, c:queue3, d:queue4, e:queue5}
            data_dict = {a:data1, b:data2, c:data3, d:data4, e:data5}
            i_dict = {a:i1, b:i2, c:i3, d:i4, e:i5}
            while True:
              if first:
                deque_dict[phase] = deque([phase, result])
              else:
                deque_dict[phase].append(result)
              temp = calculate(deque_dict[phase], data_dict[phase], i_dict[phase])
              result, code, index = temp
              if code == '4':
                i_dict[phase] = index + 1
              if phase == e:
                first = False
                if code != '4':
                  break
              phase = phase_dict[phase]
            if result > maximum[0]:
              maximum = result, (a, b, c, d, e)

print('Highest signal: ' + str(maximum[0]) + ' from sequence ' + str(maximum[1])[1:-1])