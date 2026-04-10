class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openOf = {")": "(", "]" : "[", "}" : "{"}
        
        for c in s:
            if c in openOf:
                if stack and stack[-1] == openOf[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False