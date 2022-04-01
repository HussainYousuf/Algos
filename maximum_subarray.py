def max_sub(arr):
    sum = max_sum = 0
    acc = max_acc = []
    for i in arr:
        if(i == 0):
            continue
        acc.append(i)
        sum += i
        if(sum < 0):
            acc = []
            sum = 0
        if(sum > max_sum):
            max_sum = sum
            max_acc = acc[:]
    return [max_sum, max_acc]


print(
    max_sub(
        [13, -3, -25, 20, -3, -16, -23,
         18, 20, -7, 12, -5, -22, 15, -4, 7]
    )
)