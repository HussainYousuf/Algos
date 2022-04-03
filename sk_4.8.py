def main(xs, x):
    holder = {}
    for i in xs:
        j = holder.get(i)
        if(j):
            return (j, i)
        else:
            holder[x - i] = i
    return False


print(main([1, 2, 2, 3, 5], 9))
