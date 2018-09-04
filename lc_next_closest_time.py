# Brute force
# def nextClosestTime(time):
    """
    :type time: str
    :rtype: str
    """
    hours = int(time[:2])
    mins = int(time[3:])
    checkSet = set(time[0:2] + time[3:])
    validNextNotFound = True
    while validNextNotFound:
        mins += 1
        if mins == 60:
            mins = 0
            hours += 1
        if hours == 24:
            hours = 0
            
        newSet = set()
        newSet.add(str(mins)[0])
        if mins >= 10:
            newSet.add(str(mins)[1])
        else:
            newSet.add('0')
            
        newSet.add(str(hours)[0])
        if hours >= 10:
            newSet.add(str(hours)[1])
        else:
            newSet.add('0')
        validNextNotFound = not newSet.issubset(checkSet)
    
    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    
    if mins < 10:
        mins = '0' + str(mins)
    else:
        mins = str(mins)
        
    return hours + ':' + mins

# Faster than 12% of submissions

# check https://leetcode.com/problems/next-closest-time/solution/ for better implementation


