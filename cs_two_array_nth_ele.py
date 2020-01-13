# https://app.codesignal.com/challenge/rbwtuZjSG8zJQszCz

def twoArraysNthElement(array1, array2, n):
    a1_ptr = 0
    a2_ptr = 0
    while a1_ptr < len(array1) and a2_ptr < len(array2) and n > 0:
        if array1[a1_ptr] <= array2[a2_ptr]:
            a1_ptr += 1
        else:
            a2_ptr += 1
        n -= 1
        
    if a1_ptr == len(array1):
        return array2[a2_ptr + n]
    if a2_ptr == len(array2):
        return array1[a1_ptr + n]
    return min(array1[a1_ptr], array2[a2_ptr])

