# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        t = head
        while(t):
            size+=1
            t=t.next
        if( size < 2 ): return head

        def merge(node,size):
            if( size == 1 ): return ListNode(node.val)
            
            ls = size//2
            rs = size - ls 
            ll = merge(node,ls)
            for i in range(0,ls): node = node.next 
            rl = merge(node,rs)

            nroot =  ListNode(-1)
            node = nroot
            while( ll or rl ):
                if( ll and rl ):
                    if( ll.val < rl.val ):
                        node.next = ll
                        ll = ll.next
                        node = node.next
                    else:
                        node.next = rl
                        rl = rl.next
                        node=node.next
                elif(ll):
                    node.next = ll 
                    ll = ll.next
                    node =node.next
                else:
                    node.next = rl
                    rl = rl.next
                    node = node.next
            return nroot.next

        
        return merge(head,size)
