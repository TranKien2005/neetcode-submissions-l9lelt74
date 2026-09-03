class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numberList = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (numberList.containsKey(target - nums[i])) {
                return new int[]{numberList.get(target - nums[i]), i};
            }
            if (numberList.containsKey(nums[i])) {
                continue;
            }
            numberList.put(nums[i], i);
        }

        return new int[]{};
    }
}
