def binSearch(nums, target, low, high):
    # base case
    if low > high:
        return -1

    mid = (low + high) // 2
    if target == nums[mid]:
        return mid
    if target < nums[mid]:  # taking left array
        return binSearch(nums, target, low, mid - 1)
    else:  # taking right array
        return binSearch(nums, target, mid + 1, high)


class Solution:

    def search(self, nums: List[int], target: int) -> int:

        return binSearch(nums, target, 0, len(nums) - 1)
