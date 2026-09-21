class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def invert_linked_list(head):
    previous = None
    node = head
    while node is not None:
        temp = node.next
        node.next = previous
        previous = node
        node = temp
    return previous
