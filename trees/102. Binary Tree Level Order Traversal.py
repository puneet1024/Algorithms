#For a level order traversal, we make use of a data structure called queue to store the left and right nodes of a root
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        queu = []
        queu.append(root)
        while(queu is not None):
            root = queu.pop(0)
            print(root.val,end=" ")
            if root.left:
                queu.append(root.left)
            if root.right:
                queu.append(root.right)
        return root