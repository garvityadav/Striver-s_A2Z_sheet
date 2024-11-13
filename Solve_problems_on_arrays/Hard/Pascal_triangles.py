class pascalsTriangle:
    def printWholeTriangle(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        solArr = [[1]]
        for i in range(1, numRows):
            temp = [1]  # first element is always 1
            for j in range(1, i):
                temp.append(solArr[i-1][j-1]+solArr[i-1][j])
            temp.append(1)
            solArr.append(temp)
        return solArr

    def printSingleRow(self, rowNumber: int) -> list[int]:
        solArr = []
        solArr.append(1)
        temp = 1
        for i in range(1, rowNumber-1):
            temp = temp*(rowNumber-i)
            temp = temp//i
            solArr.append(temp)
        solArr.append(1)
        return solArr

    def printNumber(self, n, c) -> int:
        ans = 1
        for i in range(1, c):
            ans = ans*(n-i)
            ans = ans//i
        return ans


newInstance = pascalsTriangle()

print(newInstance.printWholeTriangle(5))
print(newInstance.printSingleRow(5))
print(newInstance.printNumber(5, 3))
