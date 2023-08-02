# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        listed_tuple = [(p, q)]
        while listed_tuple:
            n1, n2 = listed_tuple.pop(0)
            if n1.val!=n2.val or bool(n1.left)^bool(n2.left) or bool(n1.right)^bool(n2.right):
                return False
            if n1.right:
                listed_tuple.append((n1.right, n2.right))
            if n1.left:
                listed_tuple.append((n1.left, n2.left))
        return True
