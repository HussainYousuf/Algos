def search(arr, val, start=0, end=None):
    if(end == None):
        end = len(arr)
    if(start >= end):
        return -1
    mid = (start + end) // 2
    if(arr[mid] == val):
        return mid
    if(arr[mid] < val):
        return search(arr, val, mid + 1, end)
    else:
        return search(arr, val, start, mid)


print([search([i for i in range(5, 10)], j) for j in range(0, 13)])
