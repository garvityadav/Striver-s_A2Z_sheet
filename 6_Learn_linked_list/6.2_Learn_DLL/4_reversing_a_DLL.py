def reverseDLL(self, head):
    curr = head
    while curr.next is not None:
        temp = curr.next
        curr.next = curr.prev
        curr.prev = temp
        curr = curr.prev

    temp = curr.next
    curr.next = curr.prev
    curr.prev = temp
    head = curr
    return head
