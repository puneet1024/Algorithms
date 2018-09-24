#top down approach

def fibo(n,memo):
    if memo[n] != None:
        return memo[n]
    if n==0 or n==1:
        result =  1
    else:
        result = fibo(n-1) + fibo(n-2)
    memo[n] = result
    return result

print(fibo(4,[]))