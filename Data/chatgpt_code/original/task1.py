# Prompt:
# Write a Python function that reverses a singly linked list and returns the new head.

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
