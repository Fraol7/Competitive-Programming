# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        p1 = head
        p2 = head.next

        while p2:
            if p2.val == p1.val:
                p1.next = p2.next
                p2 = p2.next
            else:
                p1,p2 = p1.next,p2.next
        return head
