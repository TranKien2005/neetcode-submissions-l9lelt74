# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalancedAndDepth(self, root: Optional[TreeNode]) -> (bool, int):
        if (not root):
            return (True, 0)
        else:
            lB, lD = self.isBalancedAndDepth(root.left)
            rB, rD = self.isBalancedAndDepth(root.right)
            if (not (lB and rB)):
                return (False, 0)
            elif (abs(lD - rD) > 1):
                return (False, 0)
            else:
                return (True, max(lD, rD) + 1)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedAndDepth(root)[0]