class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        leni = len(nums)
        while (i < leni):
            if nums[i] == 0:
                del (nums[i])
                leni -= 1
                count += 1
            else:
                i += 1

        for j in range(count):
            nums.append(0)
        return nums

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))