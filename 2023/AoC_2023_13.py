def find_vertical_reflections(m):
  lines = []
  for line in range(1, len(m[0])):
    width = min(len(m[0]) - line, line)
    for row in m:
      if row[line - width:line] != row[line:line + width][::-1]:
        break
    else:
      lines.append(line)
  return lines


data = [list(map(list, m.split("\n"))) for m in open("AoC_2023_13.txt").read().split("\n\n")]
part1 = part2 = 0

reflection_lines = []
for mirror in data:
  if lines := find_vertical_reflections(mirror):
    part1 += lines[0]
    reflection_lines.append(("c", lines[0]))
  else:
    lines = find_vertical_reflections(list(map(list, zip(*mirror))))
    reflection_lines.append(("r", lines[0]))
    part1 += 100 * lines[0]

for i, mirror in enumerate(data):
  for a in range(len(mirror)):
    for b in range(len(mirror[a])):
      mirror[a][b] = "#" if mirror[a][b] == "." else "."
      lines = find_vertical_reflections(mirror)
      mirror[a][b] = "#" if mirror[a][b] == "." else "."
      if diff := set(lines) - ({reflection_lines[i][1]} if reflection_lines[i][0] == "c" else set()):
        part2 += diff.pop()
        break
      else:
        mirror_t = list(map(list, zip(*mirror)))
        mirror_t[b][a] = "#" if mirror_t[b][a] == "." else "."
        lines = find_vertical_reflections(mirror_t)
        if diff := set(lines) - ({reflection_lines[i][1]} if reflection_lines[i][0] == "r" else set()):
          part2 += 100 * diff.pop()
          break
    else:
      continue
    break

print("Part 1: %d; part 2: %d" % (part1, part2))
