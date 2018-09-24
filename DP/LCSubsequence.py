def lcsubseq(t,s):
    co=[]
    dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                co.append(s[i])
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(s) -1][len(t)-1], co

print(lcsubseq("abef","acf"))