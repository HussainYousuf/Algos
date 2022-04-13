def move(n, src, tar, mid):
    if(n > 0):
        move(n-1, src, mid, tar)
        print(f"moving {n}th disk from {src} to {tar}")
        move(n-1, mid, tar, src)


move(3, 'A', 'B', 'C')
