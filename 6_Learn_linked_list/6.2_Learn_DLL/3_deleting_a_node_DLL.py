class Solution:
    def delete_node(self, head, x):
        # code here
        if head is None:
            return None
        count = 1
        tempHead = head

        if x == 1:
            if tempHead.next:
                head = tempHead.next
                head.prev = None
            else:
                head = None
            tempHead = None
            return head
        while tempHead:
            if count == x:
                # if the next is none aka last element
                if tempHead.next is None:
                    tempHead.prev.next = None
                else:
                    next_node = tempHead.next
                    tempHead.prev.next = next_node
                    next_node.prev = tempHead.prev
                tempHead = None
                return head
            count += 1
            tempHead = tempHead.next
        return head
