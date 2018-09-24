#https://www.youtube.com/watch?v=zKwwjAkaXLI

#takes two input, li is the set of numbers and su is the sum


def subset_sum(li,su):
    n = len(li)
    dp = [[0 for _ in range(su+1)] for _ in range(len(li))]
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in range(su+1):
            dp[i][j] = dp[i-1][j] or dp[i-1][j-li[i]]
    return dp[n-1][su]


print(subset_sum([1, 3, 6, 9], 17))
