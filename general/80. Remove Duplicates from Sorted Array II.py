class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leni = len(nums)
        if leni == 0:
            return 0
        if leni == 1:
            return 1
        j = 0           #to store index of next unique element
        for i in range(len(nums) - 2):
            if nums[i] != nums[i + 2]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[len(nums)-2]
        nums[j+1] = nums[len(nums)-1]
        return len(nums[0:j+2]),nums[0:j+2]

s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))