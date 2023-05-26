# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       head = ListNode(0)
       current = head
       carry = 0
       while (l1 or l2):
           a = l1.val if l1 else 0
           b = l2.val if l2 else 0
           sum = a + b + carry
           if sum >= 10:
               val = sum % 10
               carry = 1
           else:
               val = sum
               carry = 0
           current.next = ListNode(val)
           current = current.next
           if l1:
               l1 = l1.next
           if l2:
               l2 = l2.next
       if carry:
          current.next = ListNode(carry)
       return head.next
