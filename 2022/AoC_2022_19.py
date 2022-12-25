import re
from collections import deque

part2, blueprints = 1, []
for i in open("AoC_2022_19.txt").read().strip().split('\n'):
    matches = list(map(int, re.match(r'.*:.*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*', i).groups()))
    blueprints.append({
        "o": matches[0],
        "c": matches[1],
        "ob": (matches[2], matches[3]),
        "g": (matches[4], matches[5])
    })
max_blueprints, i = [], 0
for b in blueprints:
    max_ore_needed = max(b["o"], b["c"], b["ob"][0], b["g"][0])
    max_geodes = max_geodes_2 = 0
    visited = dict()
    queue = deque([(1, 0, 0, 0, 0, 0, 0, 0, 0)])  # ore, clay, obsidian, # ore, # clay, # obsidian, # geode, min
    while queue:
        limit = 32 if i < 3 else 24
        o_r, c_r, ob_r, g_r, o, c, ob, g, m = queue.popleft()
        k = (o_r, c_r, o, c, ob, ob_r)
        if k in visited and (visited[k][0] <= m and g == visited[k][1] or g <= visited[k][1] and m == visited[k][0]):
            continue
        visited[k] = (min(visited[k][0], m), max(visited[k][1], g)) if k in visited else (m, g)
        if m == 24:
            max_geodes = max(max_geodes, g)
            if i >= 3:
                continue
        elif m == 32 and i < 3:
            max_geodes_2 = max(max_geodes_2, g)
            continue
        time_left = limit - m
        # if you can't build another geode robot with 2 minutes to go, then you can't get any additional geodes
        if m >= limit - 2 and not (b["g"][0] <= o and b["g"][1] <= ob):
            if limit == 24:
                max_geodes = max(max_geodes, g + g_r * time_left)
            else:
                max_geodes_2 = max(max_geodes_2, g + g_r * time_left)
            continue
        if b["g"][0] <= o and b["g"][1] <= ob:
            queue.append((o_r, c_r, ob_r, g_r + 1, o + o_r - b["g"][0], c + c_r, ob + ob_r - b["g"][1], g + g_r, m + 1))
        else:
            if ob_r * time_left + ob < b["g"][1] * time_left and b["ob"][0] <= o and b["ob"][1] <= c:
                queue.append((o_r, c_r, ob_r + 1, g_r, o + o_r - b["ob"][0], c + c_r - b["ob"][1], ob + ob_r, g + g_r,
                              m + 1))
            else:
                if o_r * time_left + o < max_ore_needed * time_left and (
                        (b["ob"][0] > o and b["g"][1] > ob) or (b["ob"][1] > c and b["g"][1] > ob) or
                        (b["g"][0] > o and b["g"][1] <= ob)):
                    if b["o"] <= o:
                        queue.append((o_r + 1, c_r, ob_r, g_r, o + o_r - b["o"], c + c_r, ob + ob_r, g + g_r, m + 1))
                if (b["c"] > o or b["o"] > o or b["ob"][1] > c) and b["g"][1] > ob:
                    queue.append((o_r, c_r, ob_r, g_r, o + o_r, c + c_r, ob + ob_r, g + g_r, m + 1))
            if c_r * time_left + c < b["ob"][1] * time_left and b["c"] <= o and b["g"][1] > ob:
                queue.append((o_r, c_r + 1, ob_r, g_r, o + o_r - b["c"], c + c_r, ob + ob_r, g + g_r, m + 1))
    if i < 3:
        part2 *= max_geodes_2
    i += 1
    max_blueprints.append(max_geodes)
print('Part 1: %d; part 2: %d' % (sum([(i + 1) * j for i, j in enumerate(max_blueprints)]), part2))
