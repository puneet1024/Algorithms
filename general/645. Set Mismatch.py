class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sumli = sum(nums)
        sumi = 0
        li = []
        for i in range(1, len(nums) + 1):
            sumi += i
        for j in range(len(nums)):
            if nums[abs(nums[j]) - 1] > 0:
                nums[abs(nums[j]) - 1] = - nums[abs(nums[j]) - 1]
            else:
                li.append(abs(nums[j]))
        li.append(sumi - sumli + li[0])
        return li

s = Solution()
print(s.findErrorNums([1,2,2,4]))