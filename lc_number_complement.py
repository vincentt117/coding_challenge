# https://leetcode.com/problems/number-complement/description/

def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    ret = 0
    expo = 0
    while num:
        if not num % 2:
            ret += 2 ** expo
        expo += 1
        num //= 2
    return ret

# Faster than 100% of accepted submissions as 36ms
        