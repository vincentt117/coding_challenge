# https://leetcode.com/problems/plus-one/description/

def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    
    carry = 1
    i = len(digits) - 1
    while carry:
        digits[i], carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
        if carry and i == 0:
            return [1] + digits
        if not carry:
            return digits
        i -= 1
    return digits

# Faster than 100% of submissions   


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits) - 1, -1, -1):
            d_sum = digits[i] + add
            digits[i] = d_sum % 10
            add = d_sum // 10
        return [1] + digits if add == 1 else digits
            