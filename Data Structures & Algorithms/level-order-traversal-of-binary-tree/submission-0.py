# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        curr = [root]

        def bfs(curr):
                nlevel = []
                nonlocal res
                res.append([])
                for node in curr:
                    res[-1].append(node.val)
                    if (node.left):
                        nlevel.append(node.left)
                    if (node.right):
                        nlevel.append(node.right)
                if len(nlevel) == 0:
                    return
                bfs(nlevel)
        bfs(curr)
        return res