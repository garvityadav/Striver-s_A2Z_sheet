class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        # code here
        if head is None:
            return Node(x)
        curr = head
        while curr.next is not None:
            curr = curr.next

        node = Node(x)
        curr.next = node
        return head
