def brute_pattern(a, p):
    m = len(a)
    n = len(p)

    for i in range(0, m-n+1):
        for j in range(0, n):
            if a[i+j] != p[j]:
                break
        if j == n-1:
            return i        #index where pattern occurs
    #not found
    return m


print(brute_pattern("abacadarab", "ca"))