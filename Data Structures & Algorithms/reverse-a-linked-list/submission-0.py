# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current, nt1 = head, head.next
        head.next = None
        while (not nt1 is None):
            nt2 = nt1.next
            nt1.next = current
            current, nt1 = nt1, nt2
        return current