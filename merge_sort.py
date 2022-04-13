

import math

# recursive def of merge but is not fast
# def merge(left, right, arr):
#     if(not left):
#         arr += right[:]
#     elif(not right):
#         arr += left[:]
#     elif(left[0] < right[0]):
#         arr.append(left[0])
#         merge(left[1:], right, arr)
#     else:
#         arr.append(right[0])
#         merge(left, right[1:], arr)

inversions = 0


def merge_sort(arr):
    if(len(arr) < 2):
        return
    mid = (0 + len(arr)) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)  # sort left inplace
    merge_sort(right)  # sort right inplace

    left.append(math.inf)
    right.append(math.inf)
    i = 0
    j = 0
    k = 0
    while (k < len(arr)):
        if(left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            global inversions
            inversions += (len(left) - 1)
            arr[k] = right[j]
            j += 1
        k += 1


def sort(arr):
    merge_sort(arr)
    return arr


print(sort([5, 4,3,2]))
print(inversions)
