# https://leetcode.com/problems/add-two-numbers-ii/description/

def addTwoNumbersInts(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        int1 = 0
        int2 = 0
        while l1 or l2:
            if l1:
                int1 *= 10
                int1 += l1.val
            if l2:
                int2 *= 10
                int2 += l2.val
        finalInt = int1 + int2
        head = None
        while finalInt > 0:
            headPrev = ListNode(finalInt % 10)
            finalInt //= 10
            headPrev.next = head
            head = headPrev
        return head
# Faster than 98% of solutions

def addTwoNumbersStacks(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    stack1 = []
    stack2 = []
    while l1 or l2:
        if l1:
            stack1.append(l1.val)
            l1 = l1.next
        if l2:
            stack2.append(l2.val)
            l2 = l2.next
    carry = 0 
    head = None
    while stack1 or stack2 or carry:
        v1 = 0
        v2 = 0
        if stack1:
            v1 = stack1.pop()
        if stack2:
            v2 = stack2.pop()
        store = v1 + v2 + carry
        headPrev = ListNode(store % 10)
        headPrev.next = head
        carry = store // 10
        head = headPrev
        
    return head
# Faster than 66% of solutions 