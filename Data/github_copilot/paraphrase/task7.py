def detect_repeated_node(head):
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow is fast:
			return True
	return False
