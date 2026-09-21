# Prompt:
# Write a Python function that detects whether a singly linked list contains a cycle.

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
