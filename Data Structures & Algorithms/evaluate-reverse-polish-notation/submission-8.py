class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            try:
                value = int(t)
                print(t, "is number")
                stack.append(value)
            except ValueError:
                print(t, "is operator")
                x1 = stack[-1]
                stack.pop()
                x2 = stack[-1]
                stack.pop()
                match t:
                    case "+":
                        stack.append(x1 + x2)
                    case "-":
                        stack.append(x2 - x1)
                    case "*":
                        stack.append(x1 * x2)
                    case "/":
                        stack.append(int(x2 / x1))
                
            print(stack)
        return round(stack[-1])
