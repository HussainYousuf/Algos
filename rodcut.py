import math
from functools import cache


def rodcut(arr, n):
    holder = {}

    @cache
    def _rodcut(n):
        if(n == 0):
            return [0, 0]
        max_sum = 0
        ith_price = 0
        for i in range(1, min(n+1, len(arr)+1)):
            rest_sum, rest_ith_price = _rodcut(n-i)
            sum = arr[i-1] + rest_sum
            if(sum > max_sum):
                max_sum = sum
                ith_price = arr[i-1]
                holder[rest_sum] = rest_ith_price

        return [max_sum, ith_price]

    x = _rodcut(n)
    print(holder)
    return x


print(rodcut([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 30))


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


# print(subset_sum_repeating([3, 4], 7))
