# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low, high = -1*2**32, 2**31
        def validator(root, low, high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return validator(root.left,low,root.val) and validator(root.right,root.val,high)
        return validator(root,low,high)
