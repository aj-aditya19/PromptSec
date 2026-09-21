def invert_list(head):
	previous = None
	while head:
		following = head.next
		head.next = previous
		previous, head = head, following
	return previous
