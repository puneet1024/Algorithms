#Check next element if equal, if not keep updating another index (j) to keep track of unequal characters


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
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[len(nums) - 1]
        j += 1
        return j

# Time - O(n)
# Space - O(1)