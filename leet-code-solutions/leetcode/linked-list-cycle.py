# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabb = head
        tort = head
        while rabb and rabb.next:
            rabb = rabb.next.next
            tort = tort.next
            if rabb == tort:
                return True
        return False
        