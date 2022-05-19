
def subset_sum(arr, target, acc=[]):
    if(acc and target == 0):
        return [acc]
    if(not arr):
        return [[]]

    n = arr.pop()
    return subset_sum(arr[:], target, acc) + subset_sum(arr, target - n, [*acc, n])


k = subset_sum(
    [2, 1, 0, -1], 2
)
print(k)
print(list(filter(lambda a: len(a) == 4, k)))

