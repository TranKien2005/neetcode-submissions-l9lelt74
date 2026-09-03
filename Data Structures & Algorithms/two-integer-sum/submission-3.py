class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberList = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in numberList:
                return [min(i, numberList[target - nums[i]]), max(i, numberList[target - nums[i]])]
            else:
                if nums[i] not in numberList:
                    numberList[nums[i]] = i
        
        