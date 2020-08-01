# https://leetcode.com/problems/remove-linked-list-elements/

# Optimal

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def removeNode(prev_node, node, next_node):
            if prev_node: prev_node.next = next_node
            node.next = None
            if self.ret == node: self.ret = next_node
            return next_node
        
        prev,self.ret = head, head
        while head:
            if head.val == val:
                head = removeNode(prev, head, head.next)
            else:
                prev, head = head, head.next
        return self.ret