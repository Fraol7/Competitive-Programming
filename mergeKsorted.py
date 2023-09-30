# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [] 
        dummy_list = ListNode()        
        ctr = 0 
       
        for linked_list in lists:
            if not linked_list:
                continue
            list_val = linked_list.val
            heapq.heappush(heap, (list_val, ctr, linked_list))
            ctr += 1

        if not heap:
            return None

        cur_node = dummy_list
        while heap:
            node_tuple = heapq.heappop(heap)
            node = node_tuple[2]
            node_next = node.next
            cur_node.next = node
            cur_node = cur_node.next
            
            if node_next:
                list_val = node_next.val
                new_node_tuple = (list_val, ctr, node_next)
                heapq.heappush(heap, new_node_tuple)
                ctr += 1
        return dummy_list.next
