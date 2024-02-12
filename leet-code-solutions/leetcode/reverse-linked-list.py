# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        while head and head.next:
            temp = dummy.next
            dummy.next = head.next
            head.next = head.next.next
            dummy.next.next = temp
        return dummy.next
