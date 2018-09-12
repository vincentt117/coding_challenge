# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        farNode = head
        toBeDel = head
        prev = head
        while n > 0:
            farNode = farNode.next
            n -= 1
        while farNode:
            farNode = farNode.next
            if prev != toBeDel:
                prev = prev.next
            toBeDel = toBeDel.next
        
        if toBeDel == head:
            return toBeDel.next
        prev.next = toBeDel.next

        
        return head
# Faster than 99% of submissions at 40ms

def removeNthFromEnd(self, head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
# Cleaner implementation
            