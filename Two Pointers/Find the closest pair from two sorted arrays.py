# https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/

# Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.


class Solution:
    def twoSum(self, l1,l2,target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(l2) - 1
        li = []
        min = target
        lef,rig = 0,0
        while (start <len(l1) and end >=0):
            if abs(l1[start] + l2[end] - target) < min:
                min = abs(l1[start] + l2[end] - target)
                li.append(l1[start])
                li.append(l2[end])
                lef = start
                rig = end
            elif l1[start] + l2[end] < target:
                start = start + 1
            elif l1[start] + l2[end] > target:
                end = end - 1
        return li[-2:], lef, rig

s=Solution()
print(s.twoSum([1, 4, 5, 7],[10, 20, 30, 40],50))


#Time Complexity : O(n)
# Space Complexity : O(1)