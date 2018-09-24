# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# The maximum sum at every index is max sum before plus the value at the index

#General formulae :

##at each point max value is  = max(incl , excl + nums[i]) where incl is including that number and exclusive is exclusing that number

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_sum = 0
        odd_sum = 0
        for i in range(len(nums)):
            if i%2 == 0:
                even_sum = max(even_sum+nums[i],odd_sum)
            else:
                odd_sum = max(odd_sum+nums[i],even_sum)
        return max(even_sum,odd_sum)