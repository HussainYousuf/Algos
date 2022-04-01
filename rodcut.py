import math
from functools import cache


def rodcut(arr, n):

    @cache
    def _rodcut(n, is_base_call=False):
        if(n == 0):
            return 0
        max_sum = 0
        ith_cut = 0
        for i in range(1, min(n+1, len(arr)+1)):
            sum = arr[i-1] + _rodcut(n-i)
            if(sum > max_sum):
                max_sum = sum
                ith_cut = i

        return [max_sum, ith_cut] if is_base_call else max_sum

    values = []
    max_sum, ith_cut = _rodcut(n, True)
    values.append(ith_cut)
    n = n - ith_cut
    while(n != 0):
        _, ith_cut = _rodcut(n, True)
        values.append(ith_cut)
        n = n - ith_cut
    return (max_sum, values)


print(rodcut([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 2))


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
