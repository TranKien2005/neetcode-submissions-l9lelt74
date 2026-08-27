class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> counter1 = new HashMap<>();
        HashMap<Character, Integer> counter2 = new HashMap<>();

        for (char a: s.toCharArray()) {
            counter1.put(a, counter1.getOrDefault(a, 0) + 1);
        }

        for (char b: t.toCharArray()) {
            counter2.put(b, counter2.getOrDefault(b, 0) + 1);
        }

        if (counter1.equals(counter2)) {
            return true;
        }
        return false;
    }
}
