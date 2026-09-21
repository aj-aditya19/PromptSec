# Prompt:
# Write a Python function that detects whether a singly linked list contains a cycle.

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
