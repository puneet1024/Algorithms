#Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


#Technique
# We take two pointers, one representing the first element and other representing the last element of the array, and
# then we add the values kept at both the pointers. If their sum is smaller than X then we shift the left pointer to right or
# if their sum is greater than X then we shift the right pointer to left, in order to get closer to the sum. We keep moving the pointers until we get the sum as X.



class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        li = []
        while (start <= end):
            if numbers[start] + numbers[end] > target:
                end = end - 1
            elif numbers[start] + numbers[end] < target:
                start = start + 1
            elif numbers[start] + numbers[end] == target:
                li.append(start + 1)
                li.append(end + 1)
                return li

s=Solution()
print(s.twoSum([2,7,11,15],9))

#Time Complexity - O(n)