def rec(n):
    if n <= 1:return 1
    result = 0
    for i in range(n):
        result += rec(i)* rec(n-1-i)
    return result
