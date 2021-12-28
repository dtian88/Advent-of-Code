position = [[-2, 9, -5], [16, 19, 9], [0, 3, 6], [11, 0, 11]]
velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for t in range(20):
  for i in range(len(position)):
    for j in range(i + 1, len(position)):
      for k in range(3):
        if position[i][k] > position[j][k]:
          velocity[i][k] -=1
          velocity[j][k] += 1
        elif position[i][k] < position[j][k]:
          velocity[i][k] +=1
          velocity[j][k] -= 1
  for i in range(len(position)):
    for j in range(3):
      position[i][j] += velocity[i][j]
  print(position, velocity)

energy = 0
for i in range(len(position)):
  pot = 0
  kin = 0
  for j in range(3):
    pot += abs(position[i][j])
    kin += abs(velocity[i][j])
  energy += pot * kin
print(energy)