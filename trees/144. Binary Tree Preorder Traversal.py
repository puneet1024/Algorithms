#time complexity - O(n)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        s = []
        si = []
        s.append(root)
        while len(s) is not 0:
            node = s.pop()
            si.append(node.val)
            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)
        return si

t = TreeNode(1)
t.left = None
t.right = TreeNode(2)
t.right.left = TreeNode(3)
s = Solution()
print(s.preorderTraversal(t))