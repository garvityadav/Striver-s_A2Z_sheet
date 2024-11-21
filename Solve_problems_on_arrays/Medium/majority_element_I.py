class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        targetElement = nums[0]
        for i in range(0, n):
            if nums[i] == targetElement:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    targetElement = nums[i]
                    count = 1

        count = 0
        for i in range(0, n):
            if nums[i] == targetElement:
                count += 1
        if count > n // 2:
            return targetElement


newInstance = Solution()

print(newInstance.majorityElement([2, 3, 3, 2, 3]))
