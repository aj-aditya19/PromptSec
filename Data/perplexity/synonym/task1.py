class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def invert_linked_list(head):
    """
    Write a Python method that inverts a singly linked list and outputs the new head.
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
