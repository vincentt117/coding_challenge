# Reverse Linked List

# https://leetcode.com/explore/interview/card/facebook/6/round-2-onsite-interview/318/

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

nodeHead = ListNode(1)
curr = nodeHead
for i in range(2, 3):
    curr.next = ListNode(i)
    curr = curr.next
curr.next = None

this = nodeHead
while this:
    print(this.val)
    this = this.next


def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        nextNode = head.next
        head.next = None
        while nextNode:
            temp = nextNode.next
            nextNode.next = curr
            curr = nextNode
            nextNode = temp
        return curr
    
def reverseListRecur(head):
    if not head:
        return head
    elif not head.next:
        return head
    else: 
        return reverseListRecurHelper(None, head)

def reverseListRecurHelper(left, right):
    if not right.next:
        right.next = left
        return right
    else:
        temp = right.next
        right.next = left
        return reverseListRecurHelper(right, temp)



this = reverseListRecur(nodeHead)
while this:
    print(this.val)
    this = this.next
            
            




#print(reverseList(nodeHead))