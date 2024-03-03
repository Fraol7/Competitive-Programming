# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        prev_node = dummy
        for _ in range(left - 1):
            prev_node = prev_node.next
        current = prev_node.next
        for _ in range(left,right):
            next_node = current.next
            current.next, next_node.next, prev_node.next = next_node.next, prev_node.next, next_node
        return dummy.next
