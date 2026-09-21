def contains_loop(head):
    tortoise = head
    hare = head
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return True
    return False
