'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''


def constructDLL(self, arr):
    # Code here
    self.head = Node(arr[0])
    mover = self.head
    prev = None
    for element in arr[1:]:
        node = Node(element)
        mover.next = node
        node.prev = mover
        mover = node

    return self.head
