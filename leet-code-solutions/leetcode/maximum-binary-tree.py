# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(nums, root):
            if not root or not nums:
                return
            max_val = max(nums)
            max_idx = nums.index(max_val)
            root.val = max_val
            root.left = buildTree(nums[:max_idx], TreeNode())
            root.right = buildTree(nums[max_idx+1:], TreeNode())
            return root
        return buildTree(nums,TreeNode())