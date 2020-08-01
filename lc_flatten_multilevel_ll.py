# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Optimal

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        head, tail = self.helper(head)
        return head
    
    def helper(self, head):    
        if not head: return head, head
        curr = head
        while True:
            if curr.child: # Found nested
                new_next, new_next_end = self.helper(curr.child)
                curr.child = None
                old_next = curr.next
                curr.next, new_next.prev = new_next, curr
                if old_next:
                    new_next_end.next, old_next.prev = old_next, new_next_end
                    curr = old_next
                else:
                    curr = new_next_end
            elif curr.next:
                curr = curr.next
                
            if not curr.next and not curr.child:
                return head, curr
