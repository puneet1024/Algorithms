class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        leni = len(nums)
        while i < leni:
            if nums[i] == val:
                del(nums[i])
                leni-=1
            else:
                i+=1
        return leni

s = Solution()
print(s.removeElement([1,2,2,6,7,4,2],2))