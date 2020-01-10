def countSumOfTwoRepresentations3(n, l, r):
    count = 0
    if l <= ((n // 2) + (n % 2)) <= r and not (l == r and n % 2):
        l_ptr = n // 2
        r_ptr = (n // 2) + (n % 2)
        count = min(l_ptr - l, r - r_ptr) + 1
        
    return count