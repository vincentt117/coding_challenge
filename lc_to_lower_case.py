# https://leetcode.com/problems/to-lower-case/description/

def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    
    return str.lower()

# Using built in. Faster than 100% of solutions


def toLowerCase1(str):
    """
    :type str: str
    :rtype: str
    """

    return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)
    
# Found in solution, using ASCII