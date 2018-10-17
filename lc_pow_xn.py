def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    temp = self.myPow(x, int(n / 2))
    if not n % 2:
        return temp * temp
    else:
        if n > 0:
            return x * temp * temp
        else:
            return temp * temp / x