class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if (nums[l] < nums[r]):
            return nums[l]
        
        while (l <= r):
            m = (l + r) // 2
            if (nums[m] > nums[l]):
                l = m
            elif (nums[m] < nums[l]):
                if nums[m] < nums[m - 1]:
                    return nums[m]
                else:
                    r = m
            else:
                return nums[r]
            
        return nums[m]
            