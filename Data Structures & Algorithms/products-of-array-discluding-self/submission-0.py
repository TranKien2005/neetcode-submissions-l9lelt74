class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productWithoutZero = None
        countZero = 0
        firstZeroIndex  = None
        for i in range(len(nums)):
            number = nums[i]
            if number == 0:
                countZero += 1
                if countZero == 1:
                    firstZeroIndex = i
                else:
                    break
            else:
                if productWithoutZero:
                    productWithoutZero *= number
                else:
                    productWithoutZero = number


        if countZero > 1:
            return [0] * len(nums)
        elif countZero == 1:
            return ([0] * firstZeroIndex) + [productWithoutZero] + ([0] * (len(nums) - firstZeroIndex - 1))
        else:
            return [productWithoutZero // i for i in nums] 
        