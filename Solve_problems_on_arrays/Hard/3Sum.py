nums = [-1, 0, 1, 2, -1, -4]
# sorted array = [-4,-1,-1,0,1,2]


class threeSum:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        solArr = []
        n = len(nums)

        target = 0
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:  # check duplicates
                continue
            j = i+1
            k = n-1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if target == total:
                    solArr.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif target > total:
                    j += 1
                else:
                    k -= 1

        return solArr


newInstance = threeSum()

print(newInstance.threeSum(nums))
