# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        def rec (cur: Optional[ListNode], target: int):
            if (not cur):
                return 0
            nonlocal length
            length += 1
            res = rec(cur.next, target) + 1
            if (res == target + 1):
                cur.next = cur.next.next
            return res
        i = rec(head, n)
        return head.next if length == n else head