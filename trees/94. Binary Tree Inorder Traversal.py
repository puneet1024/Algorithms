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
        if root is None:
            return []
        s = []
        si = []
        while True:
            if root is not None:
                s.append(root)
                root = root.left
            else:
                if len(s) == 0:
                    break
                root = s.pop()
                si.append(root.val)
                root = root.right
        return si

t = TreeNode(1)
t.left = None
t.right = TreeNode(2)
t.right.left = TreeNode(3)
s = Solution()
print(s.inorderTraversal(t))