class Solution:
    def pairSum(self, li):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        maxi = max(li[0], li[1])
        mini = min(li[0], li[1])
        for i in range(2, len(li)):
            if li[i] > maxi:
                maxi = li[i]
            elif li[i] > mini:
                mini = li[i]
        return maxi + mini


s=Solution()
print(s.pairSum([10, 70, 30, 40]))


#Time Analysis - O(n)