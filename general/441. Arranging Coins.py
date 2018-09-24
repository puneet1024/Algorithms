class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n >= i:
            n = n-i
            i += 1
        return i-1


s = Solution()
print(s.arrangeCoins(1))