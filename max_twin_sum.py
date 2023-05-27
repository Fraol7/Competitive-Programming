# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        List = []
        while curr:
            List.append(curr.val)
            curr = curr.next
        n = len(List) - 1
        ans = []
        for i in range(len(List)//2):
            ans.append(List[i] + List[n-i])
        ans.sort()
        ans = ans[::-1]
        return ans[0]

