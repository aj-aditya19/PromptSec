class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def flip_linked_list(head):
    """
    Create a function in Python which takes the head of a singly linked list 
    and returns its head after flipping the order of all the nodes.
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
