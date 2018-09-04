# https://leetcode.com/problems/license-key-formatting/
# def licenseKeyFormatting(S, K):
#     """
#     :type S: str
#     :type K: int
#     :rtype: str
#     """
#     x = 0
#     S = S.replace("-", "")
#     ret = ""
#     ret += S[:len(S) % K].upper()
#     S = S[len(S) % K:]
#     while S:
#         if ret:
#             ret += "-"
#         ret = ret + S[:K].upper()
#         S = S[K:]
#     return ret



# Brute with large number of built-in functions, faster than only 4% of submissions

def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    ret = ""
    gauge = 0
    for i in range(len(S) - 1, -1, -1):
        if gauge == K:
            ret = '-' + ret
            gauge = 0
        if S[i] != "-":
            if S[i].isalpha():
                ret = S[i].upper() + ret
            else:
                ret = S[i] + ret
            gauge += 1
    if ret and ret[0] == "-" :
        return ret[1:]
    return ret

# Iterative, beats 12% of submissions