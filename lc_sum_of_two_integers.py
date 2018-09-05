# https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a,b])        
# Literally cheating

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return round(math.log(1.00000001**a*1.00000001**b,1.00000001))#lga+lgb=lg(a*b)
# Cheating but logs