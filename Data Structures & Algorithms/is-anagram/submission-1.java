class Solution {
    public boolean isAnagram(String s, String t) {
        char[] s_sorted = s.toCharArray();
        char[] t_sorted = t.toCharArray();

        Arrays.sort(s_sorted);
        Arrays.sort(t_sorted);

        return Arrays.equals(s_sorted, t_sorted);
    }
}
