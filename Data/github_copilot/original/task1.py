class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def reverse_linked_list(head):
	previous = None
	current = head
	while current:
		following = current.next
		current.next = previous
		previous, current = current, following
	return previous
