def recur(nums, low, high, target):
    if (nums[high] < target):
        return high
    if (low > high):
        return -1
    mid = (low+high)//2
    if (nums[mid] == target):
        return mid
    if (nums[mid] < target):
        return recur(nums, mid+1, high, target)
    if (nums[mid] > target):
        # left side
        return recur(nums, low, mid-1, target)


class Solution:
    # User function Template for python3

    # Complete this function
    def findFloor(self, arr, k):
        high = len(arr)-1
        return recur(arr, 0, high, k)
