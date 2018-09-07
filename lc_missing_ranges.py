def findMissingRanges(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """
    ret = []
    numsSet = set(nums)
    missing = []
    for i in range(lower, upper + 1):
        if i not in numsSet:
            missing.append(i)
        else:
            if len(missing) == 1:
                ret.append(str(missing[0]))
            elif len(missing) >= 2:
                ret.append(str(missing[0]) + "->" + str(missing[-1]))
            missing = []
    if len(missing) == 1:
        ret.append(str(missing[0]))
    elif len(missing) >= 2:
        ret.append(str(missing[0]) + "->" + str(missing[-1]))
    return ret

# Solution breaks down with larger numbers

def findMissingRanges(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """
    if not nums:
        if lower == upper:
            return [str(lower)]
        else:
            return [str(lower) + "->" + str(upper)]
    
    
    if upper < nums[0] or nums[-1] < lower:
        if lower == upper:
            return [str(lower)]
        else:
            return [str(lower) + "->" + str(upper)]
        
    ret = []
    if lower < nums[0]:
        if abs(nums[0] - lower) == 1:
            ret.append(str(lower))
        else:
            ret.append(str(lower) + "->" + str(nums[0] - 1))

    for i,v in enumerate(nums):
        if i > 0 and lower <= nums[i-1] and v <= upper and abs(v - nums[i-1]) >= 2:
            if abs(v - nums[i-1]) == 2:
                ret.append(str(v-1))
            else:
                ret.append(str(nums[i-1] + 1) + "->" + str(v - 1))
    
    if nums[-1] < upper:
        if abs(upper - nums[-1]) == 1:
            ret.append(str(nums[-1] + 1))
        else:
            ret.append(str(nums[-1] + 1) + "->" + str(upper)) 
    return ret
# Faster than ~99% of accepted submissions


def findMissingRanges(self, nums, lower, upper):
    result = []
    nums.append(upper+1)
    pre = lower - 1
    for i in nums:
        if i == pre + 2:
            result.append(str(i-1))
        elif (i > pre + 2):
            result.append(str(pre + 1) + "->" + str(i -1))
        pre = i
    return result
# More concise solution, with same runtime as above