crates_input, moves = open("AoC_2022_5.txt").read().strip().split('\n\n')
# crates_start = ["MJCBFRLH", "ZCD", "HJFCNGW", "PJDMTSB", "NCDRJ", "WLDQPJGZ", "PZTFRH", "LVMG", "CBGPFQRJ"]
crates_start = ["" for _ in range(int(crates_input[-1]))]
for c in crates_input.split("\n")[:-1]:
    for i, crate in enumerate(c):
        if (i - 1) % 4 == 0 and crate.strip():
            crates_start[(i - 1) // 4] = crate + crates_start[(i - 1) // 4]
crates1 = crates_start.copy()
crates2 = crates_start.copy()
for m in moves.split("\n"):
    tokens = m.split()
    amount, stack1, stack2 = int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1
    crates1[stack2] += crates1[stack1][-amount:][::-1]
    crates1[stack1] = crates1[stack1][:-amount]
    crates2[stack2] += crates2[stack1][-amount:]
    crates2[stack1] = crates2[stack1][:-amount]
print('Part 1: %s; part 2: %s' % ("".join([c[-1] for c in crates1]), "".join([c[-1] for c in crates2])))
