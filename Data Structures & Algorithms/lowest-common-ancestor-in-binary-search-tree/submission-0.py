# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(curr, p, q):
                if (curr is None):
                    return None
                if (curr.val == p.val or curr.val == q.val):
                    return curr
                else:
                    if (curr.val >p.val and curr.val > q.val):
                        return dfs(curr.left, p, q)
                    elif ((curr.val > p.val and curr.val < q.val) or (curr.val <p.val and curr.val > q.val)):
                        return curr
                    else:
                        return dfs(curr.right, p, q)
        
        return dfs(root, p, q)