inputList = list(open("AoC_2020_1.txt"))
for i in range(len(inputList)):
    inputList[i] = int(inputList[i].rstrip())
for i in inputList:
    for j in inputList:
        for k in inputList:
            if i + j + k== 2020:
                print('%d + %d + %d = 2020; %d * %d * %d = %d'%(i, j, k, i, j, k, i * j * k))