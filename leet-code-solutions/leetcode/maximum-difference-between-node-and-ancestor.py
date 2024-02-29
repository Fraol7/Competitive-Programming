# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = 0
        def helper(root, mini=root.val, maxi=root.val):
            if not root:
                return
            self.maxDiff = max(self.maxDiff, abs(root.val-mini), abs(root.val-maxi))
            helper(root.left, min(mini, root.val), max(maxi, root.val))
            helper(root.right, min(mini, root.val), max(maxi, root.val))
        helper(root)
        return self.maxDiff
        
        