class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        temp = head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count
