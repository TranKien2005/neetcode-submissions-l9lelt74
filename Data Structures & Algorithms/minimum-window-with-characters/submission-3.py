class Solution:
    def minWindow(self, s: str, t: str) -> str:
        startCounter = collections.Counter(t)
        currentCounter = startCounter.copy()
        startSum = sum(startCounter.values())
        currentSum = startSum
        minLength = None
        lMin, rMin = None, None
        l = 0

        for r in range(len(s)):
            if s[r] in startCounter:
                
                if s[r] == s[l] and currentCounter[s[r]] <= 0:
                    l += 1
                    while (s[l] not in startCounter) or (currentCounter[s[l]] < 0):    
                        if (s[l] in startCounter):
                            currentCounter[s[l]] += 1
                        l += 1
                else:
                    currentCounter[s[r]] -= 1
                    if currentCounter[s[r]] >= 0:
                        currentSum -= 1

                if currentSum == 0 and ((minLength is None) or (minLength > (r - l + 1))):
                    minLength = r - l + 1
                    lMin, rMin = l, r
            else:
                if l == r:
                    l += 1 
            
        
        return s[lMin:rMin + 1] if minLength else ""
                