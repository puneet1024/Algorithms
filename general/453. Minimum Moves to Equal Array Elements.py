#[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 3 moves
#find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
#NOTE - incrementing n-1 elements by 1 is equal to decrementing 1 element by 1 in each iteration


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #sum1=0
        mi = min(nums)
        return sum(i-mi for i in nums)
        # for i in nums:
        #     sum1 = sum1+(i-mi)
        # return sum1


s = Solution()
print(s.minMoves([1, 2, 5, 78, 9]))