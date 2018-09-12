def buddyStrings(self, A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if len(A) != len(B):
        return False
    diff = 0
    col = set()
    aDiff = ""
    bDiff = ""
    hasDup = False
    for i, v in enumerate(A):
        if v in col:
            hasDup = True
        if v != B[i]:
            diff += 1
            aDiff += v
            bDiff += B[i]
        col.add(v)
    print(aDiff)
    print(bDiff[::-1])
    return (diff == 2 and aDiff == bDiff[::-1]) or (diff == 0 and hasDup)

# Faster than ~50% of accepted submissions at 44ms
        
        