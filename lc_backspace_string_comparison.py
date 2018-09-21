# https://leetcode.com/problems/backspace-string-compare/description/

def backspaceCompare(self, S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    sStack = []
    tStack = []
    for s in S:
        if s != "#":
            sStack.append(s)
        elif s == "#" and sStack:
            sStack.pop()
    
    for t in T:
        if t != "#":
            tStack.append(t)
        elif t == "#" and tStack:
            tStack.pop()
    return sStack == tStack

# Faster than 11% of accepted solutions at 36ms