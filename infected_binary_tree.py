# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        q = deque() 
        d = defaultdict(list) 
        if not root:
            return [] 
        q.append(root) 
        while q:
            n = len(q) 
            for _ in range(n):
                node = q.popleft() 
                if node.left:
                    q.append(node.left) 
                    d[node.val].append(node.left.val) 
                    d[node.left.val].append(node.val) 
                if node.right:
                    q.append(node.right) 
                    d[node.val].append(node.right.val) 
                    d[node.right.val].append(node.val)
        ans = [0] 
        q = deque() 
        q.append((start,-1,0)) 
        while q:
            node,par ,c= q.popleft() 
            for ch in d[node]:
                if ch!=par:
                    q.append((ch,node,c+1)) 
            ans[0]=c 
        return ans[0] 

