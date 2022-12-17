data, parts = open("AoC_2022_17.txt").read().strip(), []
rock_types = (((0, 0), (1, 0), (2, 0), (3, 0)),
              ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
              ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
              ((0, 0), (0, 1), (0, 2), (0, 3)),
              ((0, 0), (0, 1), (1, 0), (1, 1)))
rock, move = 0, 0
occupied, visited, max_heights = set(), dict(), [0 for _ in range(7)]
for i in range(1, 1000000000001):
    bl = [2, max([c[1] for c in occupied]) + 4 if occupied else 4]  # bottom-left corner
    while True:
        direction = -1 if data[move] == '<' else 1
        move = (move + 1) % len(data)
        if not any((bl[0] + x + direction, bl[1] + y) in occupied or
                   not (0 <= bl[0] + x + direction < 7) for x, y in rock_types[rock]):
            bl[0] += direction
        if any((bl[0] + x, bl[1] + y - 1) in occupied or bl[1] + y == 1 for x, y in rock_types[rock]):
            occupied.update({(x + bl[0], y + bl[1]) for x, y in rock_types[rock]})
            break
        bl[1] -= 1
    for x, y in rock_types[rock]:
        max_heights[bl[0] + x] = max(max_heights[bl[0] + x], bl[1] + y)
    highest = max(max_heights)
    normalized_heights = tuple(h - min(max_heights) for h in max_heights)
    if (rock, move, normalized_heights) in visited:
        before, before_height = visited[(rock, move, normalized_heights)]
        for val in (2022, 1000000000000):
            mod_height = -1
            for j, h in visited.values():
                if j == (val - before) % (i - before) + before:
                    mod_height = h
                    break
            parts.append((val - before) // (i - before) * (highest - before_height) + mod_height)
        break
    visited[(rock, move, normalized_heights)] = i, highest
    rock = (rock + 1) % 5
print('Part 1: %d; part 2: %d' % (parts[0], parts[1]))
