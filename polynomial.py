def evaluate (a, x, n):
    res = 0
    for i in range(1,n+1):
        res += a[i] * x**i 
        
    return res