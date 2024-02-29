# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:            
        dummynode = ListNode(-5001)
        while head:
            curr, head = head, head.next
            curr.next = None
            temp = dummynode
            while temp:
                if temp.val < curr.val:
                    prev = temp
                    temp = temp.next
                else: 
                    break
            curr.next, prev.next = prev.next, curr
        return dummynode.next



