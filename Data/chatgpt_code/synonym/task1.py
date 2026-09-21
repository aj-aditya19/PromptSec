# Prompt:
# Write a Python method that inverts a singly linked list and outputs the new head.

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
