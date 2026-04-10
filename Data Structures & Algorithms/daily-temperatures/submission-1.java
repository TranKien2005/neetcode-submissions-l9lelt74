class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Stack<int[]> stack = new Stack<>();

        for (int i = 0; i < temperatures.length; i++) {
            while ((!stack.isEmpty()) && (stack.peek()[0] < temperatures[i])) {
                res[stack.peek()[1]] = i - stack.peek()[1];
                stack.pop();
            }
            stack.push(new int[]{temperatures[i], i});
        }

        while (!stack.isEmpty()) {
            res[stack.peek()[1]] = 0;
            stack.pop();
        }

        return res;
    }
}
