def FlipBit(width, height, flipX, flipY, intArray):
    if intArray[flipY * (width) + flipX] == 0:
        intArray[flipY * (width) + flipX] = 1
    else:
        intArray[flipY * (width) + flipX] = 0

    return intArray


# [0, 0, 0, 0]
# [0, 0, 0, 1] 
# [0, 0, 0, 0]
# [0, 0, 0, 1]


def FlipBit2D(width, height, flipX, flipY, intArray):
    intArray = [intArray[width * (h-1):width * h] for h in range(1, height + 1)]
    if intArray[flipY][flipX] == 0:
        intArray[flipY][flipX] = 1
    else:
        intArray[flipY][flipX] = 0
    ret = []
    return [ret + i for i in intArray]