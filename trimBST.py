# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
        if not root:
            return None
        node = root
        while node:
            while node.left and node.left.val < low:
                node.left = node.left.right
            node = node.left
        node = root
        while node:
            while node.right and node.right.val > high:
                node.right = node.right.left
            node = node.right
        return root
