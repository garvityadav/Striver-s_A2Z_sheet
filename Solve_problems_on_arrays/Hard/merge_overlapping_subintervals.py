intervals = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]


class mergeOverlappingSubIntervals:
    def optimalApproach(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        solArr = [intervals[0]]
        maxNum = solArr[0][1]
        index = 0
        for i in range(1, n):
            if intervals[i][0] <= maxNum:
                maxNum = max(solArr[index][1], intervals[i][1])
                solArr[index] = ([solArr[index][0],
                                  maxNum])
            else:
                solArr.append(intervals[i])
                index += 1
                maxNum = intervals[i][1]
        return solArr


print(mergeOverlappingSubIntervals().optimalApproach(intervals))
