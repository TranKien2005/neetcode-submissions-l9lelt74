class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        while (i < j):
            while(not s[i].isalnum()):
                if i >= j:
                    break
                i += 1
            while(not s[j].isalnum()):
                if i >= j:
                    break
                j -= 1
            if i >= j:
                break
            if (s[i] == s[j]):
                print(s[i], s[j])
                i += 1
                j -= 1
            else:
                return False
        return True        