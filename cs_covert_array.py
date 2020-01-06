# Convert arrays from Code Signal
# Walk through array until completion (length guranteed to be size 2^k, where k is an integer)
# On each odd num iteration (1, 3, 5, etc.,) add each pair of numbers
# On each even num iteration (2, 4, 6, etc.,) multiply each pair of numbers
# Return the result integer

def arrayConversion(inputArray):
    return helper(inputArray)

def helper(inputArray):
    n = len(inputArray)
    if n == 1:
        return inputArray[0]
    if n == 2:
        return [inputArray[0] + inputArray[1], 2]
    left = helper(inputArray[:n//2])
    right = helper(inputArray[n//2:])
    incre = left[1] + 1
    if left[1] % 2:
        return [left[0] + right[0], incre]
    else:
        return [left[0] * right[0], incre]

# i.e., [1, 2, 3, 4, 5, 6, 7, 8] -> 186