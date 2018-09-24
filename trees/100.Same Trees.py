# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        qu1 = []
        qu2 = []

        if p is None or q is None:
            return False
        qu1.append(p)
        qu2.append(q)
        while(p is not None or q is not None):
            if(p.x != q.x):
                return False
            else:
                
