def lcp(s,t):
    minl = min(len(s),len(t))
    for i in range(minl):
        if s[i] != t[i]:
            return i
        return minl

print(lcp("a","b"))