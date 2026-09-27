class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_loop(head):
    """
    Write a Python method that identifies whether a singly linked list has a loop.
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
