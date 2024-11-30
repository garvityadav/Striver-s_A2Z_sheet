num1 = [1, 8, 8]
num2 = [2, 3, 4, 5]
m = 3
n = len(num2)


class mergeSortedArray:
    def solutionForCodingNinjas(self, num1: list[int], num2: list[int]):
        m = len(num2)
        for i in range(0, m):
            num1.append(num2[i])
        n = len(num1)
        gap = n//2 + n % 2

        while gap > 0:
            left = 0
            right = gap
            while right < n:
                if num1[left] > num1[right]:
                    num1[left], num1[right] = num1[right], num1[left]
                left += 1
                right += 1
            if gap == 1:
                break
            gap = gap//2 + gap % 2


newInstance = mergeSortedArray()
print(newInstance.solutionForCodingNinjas(num1, num2))

print(num1)
