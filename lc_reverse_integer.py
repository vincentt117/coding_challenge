# https://leetcode.com/problems/reverse-integer/description/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        factor = cmp(x, 0) # this
        # does this
        # if x < 0:
        #     factor = -1
        # else:
        #      factor = 1

        x = abs(x)
            
        store = 0
        while x > 0:
            store = store*10 + (x % 10)
            x //= 10
        
        if -2**31 <= (store*factor) <= 2**31 - 1:
            return store * factor
        return 0

# Fast, faster than 85% of submissions at 32ms. With cmp(), faster than 100% of solutions
        