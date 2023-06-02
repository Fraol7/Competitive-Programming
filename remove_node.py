# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stak = []                                          
        curr = head

        while curr:                                         
            while stak and curr.val > stak[-1].val:        
                stak.pop()                                 
            stak.append(curr)                               
            curr = curr.next                                  
        dumm = ListNode()                                  
        curr = dumm
        for node in stak:                                  
            curr.next = node                                 
            curr = curr.next                                  
        return dumm.next                                   
