# https://leetcode.com/problems/lemonade-change/description/
def lemonadeChange(self, bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    fiveCount = 0
    tenCount = 0
    for i in bills:
        if i == 5:
            fiveCount += 1
        elif i == 10 and fiveCount > 0:
            fiveCount -= 1
            tenCount += 1
        elif i == 20:
            if fiveCount > 0 and tenCount > 0:
                fiveCount -= 1
                tenCount -= 1
            elif fiveCount >= 3:
                fiveCount -= 3
            else:
                return False
        else:
            return False
    return True

# Faster than 100% of accepted solutions at 28ms
            
    