# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ctrA, ctrB = 0, 0
        currA, currB = headA, headB
        while currA:
            ctrA += 1
            currA = currA.next
        while currB:
            ctrB += 1
            currB = currB.next
        
        new_currA = headA
        new_currB = headB
        if ctrA >= ctrB:
            while ctrA > ctrB:
                new_currA = new_currA.next
                ctrA -= 1
        else:
            while ctrA < ctrB:
                new_currB = new_currB.next
                ctrB -= 1
        while new_currB:
            if new_currB == new_currA:
                return new_currA
            new_currA = new_currA.next
            new_currB = new_currB.next
        return 
