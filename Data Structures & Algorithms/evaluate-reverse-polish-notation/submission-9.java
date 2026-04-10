class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String s: tokens) {
            System.out.print(s + " ");
            System.out.println(stack.size());
            try {
                int value = Integer.parseInt(s);
                stack.push(value);
            }
            catch (Exception e) {
                int n2 = stack.peek();
                stack.pop();
                int n1 = stack.peek();
                stack.pop();

                if (s.equals("+")) {
                    stack.push(n1 + n2);
                }
                else if (s.equals("-")) {
                    stack.push(n1 - n2);
                }
                else if (s.equals("*")) {
                    stack.push(n1 * n2);
                }
                else if (s.equals("/")) {
                    stack.push((int) (n1 / n2));
                }
                else {
                    System.out.println("bug");
                }
            }
        }
        return stack.peek();
    }
}
