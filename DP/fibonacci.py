#bottom up approach

def fibonacci(n):
    memo = [0] * (n+1)
    print(len(memo))
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(fibonacci(10))