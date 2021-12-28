data = []

def reset():
  global data
  data = [109,424,203,1,21101,11,0,0,1106,0,282,21101,18,0,0,1106,0,259,1202,1,1,221,203,1,21102,31,1,0,1105,1,282,21101,0,38,0,1106,0,259,21002,23,1,2,22102,1,1,3,21102,1,1,1,21102,57,1,0,1106,0,303,2102,1,1,222,21002,221,1,3,20102,1,221,2,21102,1,259,1,21102,1,80,0,1105,1,225,21102,105,1,2,21102,91,1,0,1105,1,303,1202,1,1,223,20102,1,222,4,21102,259,1,3,21101,225,0,2,21101,225,0,1,21102,118,1,0,1106,0,225,20101,0,222,3,21101,157,0,2,21102,133,1,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1105,1,259,2101,0,1,223,20101,0,221,4,20101,0,222,3,21102,21,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,105,1,108,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21101,0,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1201,-4,0,249,21202,-3,1,1,21202,-2,1,2,22102,1,-1,3,21101,0,250,0,1106,0,225,22101,0,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21101,0,343,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,384,1,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0]

  for i in range(50):
    data.append(0)

def move(x, y):
  i = relative_base = 0
  seen = False
  while i < len(data):
    if data[i] == 99:
      break
    opcode = data[i] if data[i] >= -9 and data[i] <= 9 else data[i] % 10
    if opcode in range(0, 10):
      one = two = three = num_one = num_two = num_three = 0
      if data[i] >= 10000:
        three = data[i] // 10000 % 10
      if data[i] >= 1000:
        two = data[i] // 1000 % 10
      if data[i] > 100:
        one = data[i] // 100 % 10
      if one == 0:
        num_one = data[data[i + 1]]
      elif one == 1:
        num_one = data[i + 1]
      else:
        num_one = data[relative_base + data[i + 1]]
      if opcode in (1, 2, 5, 6, 7, 8):
        if two == 0:
          num_two = data[data[i + 2]]
        elif two == 1:
          num_two = data[i + 2]
        else:
          num_two = data[relative_base + data[i + 2]]
      if opcode in (1, 2, 7, 8):
        num_three = data[i + 3] if three == 0 else relative_base + data[i + 3]
      if opcode == 1 or opcode == 2:
        data[num_three] = num_one + num_two if opcode == 1 else num_one * num_two
        i += 4
      elif opcode == 3 or opcode == 4:
        if opcode == 3:
          if not seen:
            seen = True
            coordinate = x
          else:
            coordinate = y
          if one == 0:
            data[data[i + 1]] = coordinate
          else:
            data[relative_base + data[i + 1]] = coordinate
        else:
          return num_one
        i += 2
      elif opcode == 5 or opcode == 6:
        i = num_two if opcode == 5 and num_one or opcode == 6 and not num_one else i + 3
      elif opcode == 7 or opcode == 8:
        data[num_three] = 1 if num_one < num_two and opcode == 7 or num_one == num_two and opcode == 8 else 0
        i += 4
      elif opcode == 9:
        relative_base += num_one
        i += 2
    else:
      i += 1
 
reset()
# calculated from finding first point on bottom edge of tractor beam at which the beam's width is 100 (save some time)
x = 743
y = 560
while True:
  flag = True
  for i in range(99, 0, -1):
    reset()
    if not move(x - i, y + 99):
      flag = False
      break
  if flag:
    print((x - 99) * 10000 + y)
    break
  reset()
  x += 1
  if not move(x, y):
    y += 1