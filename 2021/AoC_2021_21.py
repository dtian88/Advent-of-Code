from collections import defaultdict

data = open('AoC_2021_21.txt').read().split('\n')
player_one_score = player_two_score = 0
player_one, player_two = int(data[0][-1]), int(data[1][-1])
count = count2 = 0
die = 1
while player_one_score < 1000 and player_two_score < 1000:
    c = 0
    for i in range(3):
        c += die
        die += 1
        count += 1
        if die > 100:
            die = 1
    player_one = (player_one + c) % 10
    if player_one == 0:
        player_one = 10
    player_one_score += player_one
    if player_one_score >= 1000:
        break
    c = 0
    for i in range(3):
        c += die
        die += 1
        count += 1
        if die > 100:
            die = 1
    player_two = (player_two + c) % 10
    if player_two == 0:
        player_two = 10
    player_two_score += player_two

rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}  # roll 3 times 1, 2, or 3; {sum:frequency}
frequencies1 = defaultdict(int)
frequencies1[(int(data[0][-1]), 0, -1)] = 1  # frequency of (position, score, turn number)
frequencies2 = defaultdict(int)
frequencies2[(int(data[1][-1]), 0, 0)] = 1
player = [(frequencies1, 1), (frequencies2, 2)]      # second element of tuple is turn number - starts at x for player x
for a in range(len(player)):
    frequencies, c = player[a]
    while True:
        f_copy = frequencies.copy()
        for i, j in frequencies.items():
            if i[1] >= 21 or i[2] < c - 2:
                continue
            for roll, f in rolls.items():
                new_pos = (i[0] + roll) % 10
                if new_pos == 0:
                    new_pos = 10
                f_copy[(new_pos, i[1] + new_pos, c)] += j * f
        frequencies = f_copy
        for i, j in frequencies.items():
            if i[1] < 21 and i[2] == c:
                break
        else:
            break
        c += 2
    player[a] = (frequencies, c)
p1 = p2 = 0
for i, j in player[0][0].items():
    for a, b in player[1][0].items():
        if i[2] == a[2] + 1 and i[1] >= 21 and a[1] < 21:
            p1 += j * b
        elif a[2] == i[2] + 1 and i[1] < 21 and a[1] >= 21:
            p2 += j * b
print('Part 1: %d; part 2: %d' % (min(player_two_score, player_two_score) * count, max(p1, p2)))
