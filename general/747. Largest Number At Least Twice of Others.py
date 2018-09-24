class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue = 0
        secondMaxValue = 0
        index = 0
        for i in range(len(nums)):
            if nums[i] > maxValue:
                secondMaxValue = maxValue
                maxValue = nums[i]
                index = i
            elif nums[i] > secondMaxValue:
                secondMaxValue = nums[i]
        if maxValue >= 2 * secondMaxValue:
            return index
        else:
            return -1
