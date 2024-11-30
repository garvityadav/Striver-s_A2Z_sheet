nums = [4, 2, 2, 6, 4]
k = 6


def subarraysWithSumK(a, b) -> int:
    hashMap = {0: 1}
    n = len(a)
    count = 0
    xOR = 0
    for i in range(0, n):
        xOR = xOR ^ a[i]
        x = xOR ^ b
        if x in hashMap.keys():
            count += hashMap[x]
        hashMap[xOR] = hashMap.setdefault(xOR, 0)+1
    return count


print(subarraysWithSumK(nums, k))
