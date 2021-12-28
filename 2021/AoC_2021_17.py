x, y = open('AoC_2021_17.txt').read().split('\n')[0][13:].split(', ')
x_min, x_max = tuple(map(int, x[2:].split('..')))
y_min, y_max = tuple(map(int, y[2:].split('..')))
max_y = 0
velocities = set()
for i in range(1, 250):
    for j in range(-150, 150):
        pos = [0, 0]
        velocity = [i, j]
        initial_velocity = (i, j)
        prev_max = max_y
        while pos[0] <= x_max and pos[1] >= y_min:
            if pos[1] > max_y:
                max_y = pos[1]
            if x_min <= pos[0] <= x_max and y_min <= pos[1] <= y_max:
                velocities.add(initial_velocity)
                break
            pos[0] += velocity[0]
            pos[1] += velocity[1]
            if velocity[0] != 0:
                velocity[0] += -velocity[0] / abs(velocity[0])
            velocity[1] -= 1
        else:
            max_y = prev_max
print('Part 1: %d; part 2: %d' % (max_y, len(velocities)))
