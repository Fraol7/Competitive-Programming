# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow
