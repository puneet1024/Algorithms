#Whenever the value changes


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return []
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root.val

t = TreeNode(1)
t.left = TreeNode(3)
t.right = TreeNode(5)
t.right.left = TreeNode(8)
t.left .left= TreeNode(6)
t.right.right = TreeNode(2)
t.right.left.right = TreeNode(9)
t.right.left.left = TreeNode(10)
s = Solution()
print(s.lowestCommonAncestor(t,t.right,t.right.right))


