# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterAndDepth(self, root: Optional[TreeNode]) -> (int, int):
        if root is None:
            return (0, 0)
        else:
            diaLeft, depLeft = self.diameterAndDepth(root.left)
            diaRight, depRight = self.diameterAndDepth(root.right)
            return (max(depLeft + depRight , diaLeft, diaRight), max(depLeft, depRight) + 1)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterAndDepth(root)[0]