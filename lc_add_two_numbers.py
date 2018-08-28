# Add Two Numbers

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     if not l2 and l1:
    #         return l1
    #     if not l1 and l2:
    #         return l2
    #     elif not l1 and not l2:
    #         return None
    #     else:
    #         val1 = 0
    #         digit1 = 1
    #         val2 = 0
    #         digit2 = 1
    #         curr1 = l1
    #         curr2 = l2
    #         while curr1 or curr2:
    #             if curr1:
    #                 val1 += curr1.val * digit1
    #                 digit1 *= 10
    #                 curr1 = curr1.next
    #             if curr2:
    #                 val2 += curr2.val * digit2
    #                 digit2 *= 10
    #                 curr2 = curr2.next
    #         total = val1 + val2
    #         head = ListNode(0)
    #         curr = head
    #         while total > 0:
    #             curr.val = total % 10
    #             total = total // 10
    #             if total > 0:
    #                 curr.next = ListNode(None)
    #                 curr = curr.next
    #             else:
    #                 curr.next = None
    #         return head
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next

# My solution: faster than 3% of all submissions