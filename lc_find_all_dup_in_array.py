def findDuplicates(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            res.append(abs(nums[i]))
        else:
            nums[idx] = -nums[idx]
            
    return res