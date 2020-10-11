def fib(n, previous):
    previous[1] = 1
    previous[2] = 1
    i = n - 1
    while i < n:
        if i in previous.keys():
            previous[i + 1] = previous[i] + previous[i - 1]
            i += 1
        else:
            i -= 1
    return previous[n]
        
p = {}
print(fib(10, p))
