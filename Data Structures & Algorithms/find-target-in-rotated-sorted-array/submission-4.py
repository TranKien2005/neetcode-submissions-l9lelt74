class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l, r = 0, length - 1
        while (l < r):
            m = (l + r) // 2
            if (nums[m] > nums[r]):
                l = m + 1
            else:
                r = m
        pivot = l

        if target <= nums[-1]:
            l, r = pivot, length -1
        else:
            l, r = 0, (pivot - 1 + length) % length
        while (l <= r):
            m = (l + r) // 2
            if (nums[m] == target):
                return m
            elif (nums[m] < target):
                l = m + 1
            else:
                r = m - 1
        return -1