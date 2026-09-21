# Prompt:
# Write a Python method that inverts a singly linked list and outputs the new head.

# Python solution below

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    previous = None
    while head:
        following = head.next
        head.next = previous
        previous, head = head, following
    return previous
