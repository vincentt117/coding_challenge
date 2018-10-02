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
    