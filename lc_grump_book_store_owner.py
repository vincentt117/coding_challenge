# https://leetcode.com/problems/grumpy-bookstore-owner/

import collections

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        guranteed = 0
        for i, v in enumerate(customers):
            if not grumpy[i]:
                guranteed += v
        
        get_if_chill = 0
        get_if_chill_stack = collections.deque()
        max_get = guranteed
        i = 0
        while i < len(grumpy):
            if len(get_if_chill_stack) == X:
                get_if_chill -= get_if_chill_stack.popleft()
            add_cust = grumpy[i] * customers[i]
            get_if_chill += add_cust
            get_if_chill_stack.append(add_cust)
            max_get = max(max_get, get_if_chill + guranteed)
            i += 1
        return max_get
                
            
        
        
        