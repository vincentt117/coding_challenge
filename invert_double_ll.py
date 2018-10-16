def invDLL (head):
	if not head or not head.next:
		return head
	else:
		first = None
		second = head
		third = head.next
		while third:
			newCenter = third
			head.prev, head.next = third, first
			first = head
			second = newCenter
			third = second.next
		second.next = first
		second.prev = None
		return second 
# Solution not verified