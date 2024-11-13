nums = [1, 0, -1, 0, -2, 2]
target = 0


class FourSum:

    # Brute Force
    def bruteForceMethod(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        uniqueSet = set()
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        sum = nums[i]+nums[j]+nums[k]+nums[l]
                        if sum == target:
                            newList = [nums[i], nums[j], nums[k], nums[l]]
                            sortedList = tuple(sorted(set(newList)))
                            if sortedList not in uniqueSet:
                                uniqueSet.add(sortedList)
                                ans.append(newList)
            return ans

    # better approach

    def betterApproach(self, nums: list[int], target: int) -> list[list[int]]:
        solList = []
        uniqueSet = set()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1, n):
                hashMap = dict()
                for k in range(j+1, n):
                    sum = nums[i]+nums[j]+nums[k]
                # print(f'value of sum: {sum}')
                # print(f'hashMap till now---> {hashMap}')
                    remaining_element = target-sum
                    if remaining_element in hashMap.keys():
                        total = sorted(
                            [nums[i], nums[j], nums[k], remaining_element])
                        sortedList = tuple(set(total))
                        if sortedList not in uniqueSet:
                            solList.append(total)
                            uniqueSet.add(sortedList)
                #         print(f"answer = {solList}")
                    hashMap[nums[k]] = k
        return solList

    # Optimal solution

    def optimalApproach(self, nums: list[int], target: int) -> list[list[int]]:
        solList = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = n-1
                while k < l and l > k:
                    total = [
                        nums[i], nums[j], nums[k], nums[l]]
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        solList.append(total)
                        while k < l and nums[k] == nums[k+1]:
                            k += 1
                        while k < l and nums[l] == nums[l-1]:
                            l -= 1
                        k += 1
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        l -= 1
        return solList


newInstance = FourSum()

print(newInstance.bruteForceMethod(nums, target))
print(newInstance.betterApproach(nums, target))
print(newInstance.optimalApproach(nums, target))
