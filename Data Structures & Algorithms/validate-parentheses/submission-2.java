class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> openOf = new HashMap<>();
        openOf.put(')', '(');
        openOf.put(']', '[');
        openOf.put('}', '{');
    
        for (char c : s.toCharArray()) {
            if (openOf.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == openOf.get(c)) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else {
                stack.push(c);
            }
        }

        if (stack.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}
