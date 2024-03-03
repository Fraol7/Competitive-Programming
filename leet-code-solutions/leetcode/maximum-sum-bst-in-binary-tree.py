# Definition for a binary tree root.
# class Solution:
#     class TreeNode:
#         def __init__(self, val=0, left=None, right=None):
#           self.val = val
#           self.left = left
#           self.right = right
class Solution:
    def maxSumBST(self, root:TreeNode) -> int:
        self.max_sum = 0
        def isValid(root, mini, maxi):
            if maxi <= root.val or mini >= root.val:
                return False
            return True
        def helper(root):
            if not root:
                return 0, 4*10**4, -4*10**4
            totalLeft, miniLeft, maxiLeft = helper(root.left)
            totalRight, miniRight, maxiRight = helper(root.right)
            if isValid(root,maxiLeft,miniRight):
                curr_sum = totalLeft + totalRight + root.val
                self.max_sum = max(self.max_sum, curr_sum)
                miniLeft, maxiRight = min(miniLeft, root.val), max(maxiRight, root.val)
                return curr_sum, miniLeft, maxiRight
            else:
                return -4*10**4, 0, 0
        helper(root)
        return self.max_sum

        