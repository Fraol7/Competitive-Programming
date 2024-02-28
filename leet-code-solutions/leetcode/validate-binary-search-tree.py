# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, mini, maxi):
            if not root:
                return True
            if maxi <= root.val or mini >= root.val:
                return False
            return isValid(root.left, mini, root.val) and isValid(root.right, root.val, maxi)
        return isValid(root, -1*2**32, 2**31)