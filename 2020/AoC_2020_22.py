data = open("AoC_2020_22.txt").read().split('\n\n')
player1, player2 = list(map(int, data[0].split()[2:])), list(map(int, data[1].split()[2:]))     # part 1
while player1 and player2:
    card1, card2 = player1.pop(0), player2.pop(0)
    if card1 > card2:
        player1.extend([card1, card2])
    else:
        player2.extend([card2, card1])
count = sum([player1[i] * (len(player1) - i) for i in range(len(player1))]) if player1 else \
            sum([player2[i] * (len(player2) - i) for i in range(len(player2))])

player1, player2 = list(map(int, data[0].split()[2:])), list(map(int, data[1].split()[2:]))     # part 2

def recur(p1, p2, visited):
    while p1 and p2:
        c1, c2 = p1.pop(0), p2.pop(0)
        winner = c1 > c2 if c1 > len(p1) or c2 > len(p2) else recur(p1[:c1], p2[:c2], visited.copy())
        if winner:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
        if (tuple(p1), tuple(p2)) in visited:
            return 1
        visited.add((tuple(p1), tuple(p2)))
    return len(p1) > 0

count2 = sum([player1[i] * (len(player1) - i) for i in range(len(player1))]) if recur(player1, player2, set()) else \
            sum([player2[i] * (len(player2) - i) for i in range(len(player2))])
print('Part 1: %d; part 2: %s' % (count, count2))