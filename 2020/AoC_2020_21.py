data = open("AoC_2020_21.txt").read().split('\n')
ingredients = {}    # part 1
for i in data:
    ingredients[tuple(i.split(' (contains ')[0].split())] = tuple(i.split(' (contains ')[1][:-1].split(', '))
ingredient_set, allergen_set, impossibles, possibles = set(), set(), set(), {}
for i, j in ingredients.items():
    ingredient_set = ingredient_set.union(set(i))
    allergen_set = allergen_set.union(set(j))
for ingredient in ingredient_set:
    possible_allergen = False
    for allergen in allergen_set:
        possible_current_allergen = True
        for i, j in ingredients.items():
            if allergen in j and ingredient not in i:
                possible_current_allergen = False
                break
        if possible_current_allergen:
            possible_allergen = True
            if ingredient not in possibles:         #
                possibles[ingredient] = []          # part 2
            possibles[ingredient].append(allergen)  #
    if not possible_allergen:
        impossibles.add(ingredient)
count = sum([i.count(impossible) for i in ingredients for impossible in impossibles])
while not all(len(j) == 1 for i, j in possibles.items()):     # part 2
    for possible, possible_list in possibles.items():
        if len(possible_list) == 1:
            for i, j in possibles.items():
                if i != possible and possible_list[0] in j:
                    j.remove(possible_list[0])
pt2 = sorted(possibles.items(), key=lambda item: item[1])
print('Part 1: %d; part 2: %s' % (count, ''.join([i[0] + ',' for i in pt2])[:-1]))