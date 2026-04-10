class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
                    
        HashMap<Character, Integer> hashS = new HashMap<>();
        HashMap<Character, Integer> hashT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            hashS.put(s.charAt(i), hashS.getOrDefault(s.charAt(i), 0) + 1);
            hashT.put(t.charAt(i), hashT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return hashS.equals(hashT);
    }
}
