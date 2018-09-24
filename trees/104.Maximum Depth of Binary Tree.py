#Given a binary tree, find its maximum depth
#Given binary tree [3,9,20,null,null,15,7]
#its depth = 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        head = root
        if head is None:
            return 0
        else:
            left = self.maxDepth(head.left)
            right = self.maxDepth(head.right)
        return 1+max(left,right)  #root plus height of the subsequent subtree


t = TreeNode(1)
t.left = None
t.right = TreeNode(2)
t.right.left = TreeNode(3)
s = Solution()
print(s.maxDepth(t))

