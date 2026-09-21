class Node:
    def __init__(self, item):
        self.item = item
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self) -> None:
        """
        This reverses the linked list order.
        """
        prev = None
        current = self.head

        while current:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev
