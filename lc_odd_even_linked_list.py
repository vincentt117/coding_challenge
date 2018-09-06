# https://leetcode.com/problems/odd-even-linked-list/description/

def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    
    oddTail = head
    evenHead = head.next
    evenTail = head.next
    
    oddTail.next = head.next.next
    if oddTail.next:
        oddTail = oddTail.next
    else:
        oddTail.next = evenHead
        return head

    evenTail.next = None
    
    while oddTail and oddTail.next:
        evenTail.next = oddTail.next
        oddTail.next = oddTail.next.next
        
        evenTail = evenTail.next
        evenTail.next = None
        if oddTail.next:
            oddTail = oddTail.next
    
    oddTail.next = evenHead
    return head

# Faster than ~42% of accepted submissions


def oddEvenList(head):
    dummy1 = odd = ListNode(0)
    dummy2 = even = ListNode(0)
    while head:
        odd.next = head
        even.next = head.next
        odd = odd.next
        even = even.next
        head = head.next.next if even else None
    odd.next = dummy2.next
    return dummy1.next
# More concise solution, but slightly slower 
