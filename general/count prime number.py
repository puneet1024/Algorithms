#Sieve of eratothenes
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return 0
        li = [False] * (n)
        pri = []
        for i in range(2,int(n**0.5)+1):
            if li[i] == False:
                for j in range(i*i,n,i):
                    li[j] = True
        for i in range(len(li)):
            if li[i] == False:
                pri.append(i)
        return len(pri)-2

s = Solution()
print(s.countPrimes(10))