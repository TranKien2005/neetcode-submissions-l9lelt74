class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        res = r
        l = 0
        while (l <= r):
            m = (l + r + 1) // 2
            print (l, m, r, res)
            counter = 0
            if (m == 0):
                break
            for pile in piles:
                counter += (pile // m)
                if pile % m != 0:
                    counter += 1
            if counter <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        print(l, m, r, res)
        return res
                    
