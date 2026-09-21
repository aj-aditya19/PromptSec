def reverse_linked_list(head):
	previous = None
	current = head
	while current:
		next_node = current.next
		current.next = previous
		previous, current = current, next_node
	return previous
