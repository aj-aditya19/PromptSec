def flip_list(head):
	previous = None
	current = head
	while current:
		following = current.next
		current.next = previous
		previous, current = current, following
	return previous
