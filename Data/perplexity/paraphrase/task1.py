# Prompt:
# Create a function in Python which takes the head of a singly linked list and returns its head after flipping the order of all the nodes.

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
