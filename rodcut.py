import math


def rodcut(arr, n):
    if(n == 0):
        return 0
    maxPrice = -math.inf
    for i in range(1, n+1):
        maxPrice = max(arr[i-1] + rodcut(arr, n-i), maxPrice)
    return maxPrice

    # [0......................10]
    # [1 5 8 9 10 17 17 20 24 30]


print(rodcut([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 5))


def subset_sum_repeating(arr, target, sum=0, acc=[]):
    if(target == sum):
        return acc
    if(not arr or sum > target):
        return False
    new_arr = arr[:]
    new_acc = acc[:]
    new_acc.append(arr[0])
    res = subset_sum_repeating(new_arr, target, sum + arr[0], new_acc)
    if(res != False):
        return res
    new_arr = arr[:]
    new_acc = acc[:]
    new_arr.pop(0)
    return subset_sum_repeating(new_arr, target, sum, new_acc)


print(subset_sum_repeating([3, 4], 7))
