/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> hash_node = new HashSet<>();
        ListNode curr = head;
        while (curr != null) {
            if (hash_node.contains(curr)) {
                return true;
            }
            hash_node.add(curr);
            curr = curr.next;
        }
        return false;
    }
}
