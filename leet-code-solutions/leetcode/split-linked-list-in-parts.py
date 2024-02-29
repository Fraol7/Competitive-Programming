# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer, length, curr = [], 0, head
        while curr:
            length += 1
            curr = curr.next
        if length >= k: 
            quot = length // k
            remain = length % k 
            start = end = head          
            while end:
                q_temp = quot
                while q_temp:
                    q_temp -= 1
                    if q_temp:
                        end = end.next                    
                if remain:
                    remain -= 1
                    end = end.next
                temp = end.next
                end.next = None
                answer.append(start)
                end = start = temp  
        else:           
            curr = head
            while k:
                k-=1
                if not curr:
                    answer.append(None)
                    continue
                answer.append(curr)
                temp = curr.next
                curr.next = None
                curr = temp            
        return answer
                
        