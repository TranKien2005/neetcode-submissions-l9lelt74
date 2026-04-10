class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if ((len(stack) == 0) or (stack[-1][0] >= temperatures[i])):
                stack.append((temperatures[i], i))
            else:
                while (len(stack) > 0) and (stack[-1][0] < temperatures[i]):
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append((temperatures[i], i))
        while len(stack) > 0:
            res[stack[-1][1]] = 0
            stack.pop()
        return res


