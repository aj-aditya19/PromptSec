# Prompt:
# Write a Python fucntion that detcts wether a singly linked lst contians a cycl.

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
