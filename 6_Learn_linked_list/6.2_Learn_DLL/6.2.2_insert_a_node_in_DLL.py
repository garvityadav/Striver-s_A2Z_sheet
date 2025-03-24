'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''


class Solution:
    # Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        # Code here
        tempHead = head
        count = 0
        node = Node(x)
        while tempHead is not None:
            if count != p:
                tempHead = tempHead.next
            if count == p:
                next = tempHead.next
                prev = tempHead.prev
                tempHead.next = node
                node.next = next
                node.prev = tempHead
            count += 1

        return head
