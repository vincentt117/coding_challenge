# https://leetcode.com/problems/repeated-string-match/description/

def repeatedStringMatch(A, B):
    q = (len(B) - 1) // len(A) + 1
    for i in range(2):
        if B in A * (q+i): return q+i
    return -1

# Solution found in solution section
