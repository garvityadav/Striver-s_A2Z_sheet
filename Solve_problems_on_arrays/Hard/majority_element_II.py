nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]


class majorityElement:
    def betterApproach(self, nums: list[int]) -> list[int]:
        n = len(nums)
        solArr = []
        threshold = n//3
        hashMap = {}
        for i in range(0, n):
            if nums[i] in hashMap.keys():
                hashMap[nums[i]] = hashMap[nums[i]]+1
            else:
                hashMap[nums[i]] = 1
            if hashMap[nums[i]] > threshold and nums[i] not in solArr:
                solArr.append(nums[i])
            if len(solArr) >= 2:
                return solArr
        return solArr

    def optimalApproach(sef, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 1:
            return nums
        solArr = []
        threshold = n//3
        count1 = 0
        count2 = 0
        e1 = int
        e2 = int
        for i in range(0, n):
            if count1 == 0 and e2 != nums[i]:
                e1 = nums[i]
            if count2 == 0 and e1 != nums[i]:
                e2 = nums[i]
            if e1 == nums[i]:
                count1 += 1
            if e2 == nums[i]:
                count2 += 1
            if e1 != nums[i] and e2 != nums[i]:
                count1 -= 1
                count2 -= 1

        # verification
        count1 = 0
        count2 = 0
        for i in range(0, n):
            if e1 == nums[i]:
                count1 += 1
            elif e2 == nums[i]:
                count2 += 1
        if count1 > threshold:
            solArr.append(e1)
        if count2 > threshold:
            solArr.append(e2)
        return solArr


newInstance = majorityElement()

# print(newInstance.betterApproach(nums))
print(newInstance.optimalApproach(nums))
