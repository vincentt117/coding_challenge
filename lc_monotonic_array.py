# https://leetcode.com/problems/monotonic-array/description/
def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    store = A[:]
    store.sort()
    return (A == store) or (A == store[::-1])
# Faster than ~83% of submissions at 108m s

def isMonotonic(self, A):
    store = 0
    for i in xrange(len(A) - 1):
        c = cmp(A[i], A[i+1])
        if c:
            if c != store != 0:
                return False
            store = c
    return True
# One pass in Python 2