# https://leetcode.com/problems/linked-list-random-node/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from random import randint

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        checkPointer = head
        self.llLength = 0
        while checkPointer:
            self.llLength += 1
            checkPointer = checkPointer.next
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        pointer = self.head
        for i in range(1, randint(1, self.llLength)):
            pointer = pointer.next
        return pointer.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Faster than 85% of accepted submissions at 80 ms