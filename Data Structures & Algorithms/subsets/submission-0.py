class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(current.copy())
            else:
                current.append(nums[i])
                dfs(i + 1)
                current.pop()
                dfs(i + 1)
        dfs(0)
        return res