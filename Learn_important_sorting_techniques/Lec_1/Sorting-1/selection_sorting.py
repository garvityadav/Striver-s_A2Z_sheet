def selectionSort(arr, n):
    # check if arr is not empty
    if len(arr) <= 1:
        return arr
    for i in range(0, n):
        min = i
        for j in range(i, n):
            if arr[j] < arr[min]:
                min = j
        # swap
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr


print(selectionSort([4, 3, 1, 2], 4))
