def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    
    sPlacements = collections.defaultdict(list)
    tPlacements = collections.defaultdict(list)
    for i, v in enumerate(s):
        sPlacements[v].append(i)
    for j, w in enumerate(t):
        tPlacements[w].append(j)
        
    print(sPlacements.values())
    print(tPlacements.values())
    
    for k in sPlacements.values():
        if k not in tPlacements.values():
            return False
    
    return True

# Faster than ~34% of submissions
        
        