# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        merged = head
        while list1 or list2:
            if not list2:
                merged.next = list1
                break
            elif not list1:
                merged.next = list2
                break
            elif list1.val <= list2.val:
                merged.next = list1
                merged = list1
                list1 = list1.next
            elif list2.val < list1.val:
                merged.next = list2
                merged = list2
                list2 = list2.next
        return head.next
        