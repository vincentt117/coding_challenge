# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    two = head
    one = head
    if not two and not one:
        return False
    while two and two.next and one:
        two = two.next.next
        one = one.next
        if two is one:
            return True
    
    return False

# Faster than 97% of accepted submissions at 44ms