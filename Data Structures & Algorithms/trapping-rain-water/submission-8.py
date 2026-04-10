class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left, right = 0, len(height) - 1
        currentWater = min(height[left], height[right]) * (right - left - 1)
        currentLeftHeight, currentRightHeight = height[left], height[right]
        while left < right - 1:
            if height[left] <= currentRightHeight:
                left += 1
                currentWater -= min(height[left], currentLeftHeight)
                if height[left] > currentLeftHeight and left < right - 1:
                    currentWater += (min(height[left] - currentLeftHeight, height[right] - currentLeftHeight) * (right - left - 1))   
                    currentLeftHeight = height[left] 
            else:
                right -= 1
                currentWater -= min(height[right], currentRightHeight)
                if height[right] > currentRightHeight and left < right - 1:
                    currentWater += (min(height[right] - currentRightHeight, height[left] - currentRightHeight) * (right - left - 1))
                    currentRightHeight = height[right]
        return currentWater