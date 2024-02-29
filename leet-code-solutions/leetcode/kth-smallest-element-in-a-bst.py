# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.store = []
        def helper(root):
            if not root:
                return
            self.store.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        self.store.sort()
        return self.store[k-1]
        