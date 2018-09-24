# https://www.youtube.com/watch?v=wdz_KouqHx4

# Given an integer n, return the number of trailing zeroes in n!.
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        pow_of_5 = 5
        no_of_zeroes = 0
        while pow_of_5 <= n:
            no_of_zeroes += n//pow_of_5
            pow_of_5 = pow_of_5*5
        return no_of_zeroes

s = Solution()
print(s.trailingZeroes(1000))
