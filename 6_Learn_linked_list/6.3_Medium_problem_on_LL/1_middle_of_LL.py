def middleNode(self, head):
    curr = head
    pointerA = head  # slow
    pointerB = head  # fast
    while pointerB is not None and pointerB.next is not None:
        pointerA = curr.next
        pointerB = curr.next.next
        curr = curr.next
    return pointerA
