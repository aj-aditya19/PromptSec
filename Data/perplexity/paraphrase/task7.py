class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_visited_node_cycle(head):
    """
    Create a function in Python that checks a singly linked list to determine if, 
    at some point, traversing it leads back to a node that was already visited.
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
