# Prompt:
# Create a function in Python that checks a singly linked list to determine if, at some point, traversing it leads back to a node that was already visited.

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
