# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root, score):
            if not root.left and not root.right:
                return score+root.val
            left, right = 0, 0
            score += root.val
            if root.left:
                left = helper(root.left, 10*score)
            if root.right:
                right = helper(root.right, 10*score)
            return left + right
        return helper(root, 0)
