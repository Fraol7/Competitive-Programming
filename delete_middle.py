# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None

        slow, fast = head, head
        curr = None
        while fast and fast.next:
            curr = slow
            slow = slow.next
            fast = fast.next.next
        curr.next = slow.next
        return head
