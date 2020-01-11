def shuffledArray(shuffled):
    sum = 0
    for i in shuffled:
        sum += i
    shuffled.pop(shuffled.index(sum // 2))
    shuffled.sort()
    return shuffled