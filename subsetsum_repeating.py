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


print(subset_sum_repeating([3, 4], 71))