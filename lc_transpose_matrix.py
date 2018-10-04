# https://leetcode.com/problems/transpose-matrix/description/

def transpose(A):
        ret = []
        for i in range(len(A[0])):
            row = []
            for j in range(len(A)):
                row.append(A[j][i])
            ret.append(row)
        return ret

# Faster than 85% of accepted submissions at 64ms