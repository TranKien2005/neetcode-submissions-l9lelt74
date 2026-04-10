class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        currentCounter = counter.copy()
        suml = sum(currentCounter.values())
        sumCurrent = suml
        l = 0
        for r in range(len(s2)):
            if s2[r] not in counter:
                l = r + 1
                currentCounter = counter.copy()
                sumCurrent = suml
                continue
            elif currentCounter.get(s2[r], 0) <= 0:
                while currentCounter.get(s2[r], 0) <= 0:
                    currentCounter[s2[l]] += 1
                    l += 1
                    sumCurrent += 1
            currentCounter[s2[r]] -= 1
            sumCurrent -= 1
            if sumCurrent == 0:
                return True
        return False
