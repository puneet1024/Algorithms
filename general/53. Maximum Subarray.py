#agar dp negative hai, to usme kuch bhi add kyu karna hai, uske aage vale ko mauka do
#agar dp positive hai to usme har point par add karke
#max lete raho har point par

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        dp = nums[0]
        max_num = nums[0]

        for i in nums[1:]:
            if dp > 0:
                dp+=i
            else:
                dp =i
            max_num = max(max_num,dp)
        return max_num

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))