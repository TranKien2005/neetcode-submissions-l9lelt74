class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCurrent = 0
        l = 0
        r = len(heights) - 1
        while (l < r):
            maxCurrent = max(maxCurrent, min(heights[l], heights[r]) * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxCurrent