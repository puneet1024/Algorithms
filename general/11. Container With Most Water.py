class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start =0
        end = len(height)-1
        ans =0
        while start < end:
            if height[start] <= height[end]:
                ans = max(ans,height[start] * abs(end-start))
                start +=1
            else:
                ans = max(ans,height[end] * abs(end-start))
                end -= 1
        return ans

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))

#Time Complexity - O(n)
#Space Complexity - O(1)
