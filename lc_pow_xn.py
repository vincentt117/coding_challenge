# https://leetcode.com/problems/powx-n/description/

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    temp = myPow(x, int(n / 2))
    if not n % 2:
        return temp * temp
    else:
        if n > 0:
            return x * temp * temp
        else:
            return temp * temp / x

# Results: https://leetcode.com/submissions/detail/183421168/