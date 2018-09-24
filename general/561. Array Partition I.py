def arrayPairSum(nums):
    return sum(sorted(nums[::2]))


print(arrayPairSum([4,2,1,4]))