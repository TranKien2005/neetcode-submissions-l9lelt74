class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = None
        profit = 0
        for i in prices:
            if minimum is None:
                minimum = i
            else:
                if i < minimum:
                    minimum = i
                elif profit < i - minimum:
                    profit = i - minimum
        return profit
                