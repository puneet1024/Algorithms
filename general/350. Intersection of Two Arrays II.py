class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)== 0 or len(nums2 )== 0:
            return []
        li=[]
        for i in nums1:
            if i in nums2:
                li.append(i)
        return li