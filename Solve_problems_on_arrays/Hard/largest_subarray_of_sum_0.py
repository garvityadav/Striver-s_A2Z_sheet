nums = [75, -30, -60, 51, -54, 71, -8, 0, 75]


class largestSubArray:

    def bruteForceMethod(self, arr):
        n = len(arr)
        if n <= 1:
            if arr[0] == 0:
                return 1
            return 0
        count = 0
        for i in range(0, n):
            solArr = [arr[i]]
            sum = arr[i]
            if sum == 0:
                if count < len(solArr):
                    count = len(solArr)

            j = i+1
            while j < n:
                sum += arr[j]
                solArr.append(arr[j])
                if sum == 0:
                    if count < len(solArr):
                        count = len(solArr)
                j += 1

        return count

    def betterApproach(self, arr):
        n = len(arr)
        hashMap = {}

        if n <= 1:
            if arr[0] == 0:
                return 1
            return 0

        sum = 0
        count = 0

        for i in range(0, n):
            sum += arr[i]
            if sum == 0:
                count = i+1
            else:
                if sum in hashMap.keys():
                    length = i - hashMap[sum]
                    count = max(length, count)
                else:
                    hashMap[sum] = i
        return count


newInstance = largestSubArray()

print(newInstance.betterApproach(nums))
