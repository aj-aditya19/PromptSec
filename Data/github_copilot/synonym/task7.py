def contains_loop(head):
	tortoise = hare = head
	while hare and hare.next:
		tortoise = tortoise.next
		hare = hare.next.next
		if tortoise is hare:
			return True
	return False
