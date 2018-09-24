#print the diagonals of a binary tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diagonalsbinary(self, root):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        s = []
        if root is None:
            return []
        s.append(root)
        s.append(None)
        while len(s) is not None :
            root = s.pop(0)
            if root is None:
                s.append(None)
                print("\n")
                root = s.pop(0)
                if root is None:
                    break
            while(root is not None):
                print(root.val)
                if root.left :
                    s.append(root.left)
                root = root.right


t = TreeNode(1)
t.left = TreeNode(3)
t.right = TreeNode(5)
t.right.left = TreeNode(8)
t.left .left= TreeNode(6)
t.right.right = TreeNode(2)
t.right.left.right = TreeNode(9)
t.right.left.left = TreeNode(10)
s = Solution()
s.diagonalsbinary(t)

