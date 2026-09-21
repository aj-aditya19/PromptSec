# Prompt:
# Create a function in Python that checks a singly linked list to determine if, at some point, traversing it leads back to a node that was already visited.

# Python solution below

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
