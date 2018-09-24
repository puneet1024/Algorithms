class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        li = []
        if root.left:
            self.inorderTraversal(root.left)
        li.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)


t = TreeNode(1)
t.left = None
t.right = TreeNode(2)
t.right.left = TreeNode(3)
s = Solution()
print(s.inorderTraversal(t))