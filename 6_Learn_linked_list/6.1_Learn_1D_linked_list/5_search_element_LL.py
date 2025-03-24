class Solution:
    def searchKey(self, n, head, key):
        # Code here
        temp = head
        while temp is not None:
            if (temp.data == key):
                return True
            temp = temp.next

        return False
