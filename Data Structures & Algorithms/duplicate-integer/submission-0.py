class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return True
        return False
    