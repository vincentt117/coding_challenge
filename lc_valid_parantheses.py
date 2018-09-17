# https://leetcode.com/problems/valid-parentheses/description/
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True
    checkStack = []
    for i in s:
        if i == "(":
            checkStack.append(")")
        elif i == "[":
            checkStack.append("]")
        elif i == "{":
            checkStack.append("}")
        else:
            if not checkStack or checkStack.pop() != i:
                return False
    return not checkStack

# Faster than 99% of accepted submissions
                
        