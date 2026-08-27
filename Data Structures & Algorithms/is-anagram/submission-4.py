class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1, counter2 = collections.Counter(s), collections.Counter(t)
        if (counter1 == counter2):
            return True
        return False