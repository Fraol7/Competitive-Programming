# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        def traverse(root):
            if not root:
                return 
            traverse(root.left)
            self.arr.append(root.val)
            traverse(root.right)

        def build(root, left, right):
            if left > right:
                return
            mid = left + (right-left)//2
            root.val = self.arr[mid]
            root.left = build(TreeNode(), left, mid-1)
            root.right = build(TreeNode(), mid+1, right)
            return root
        traverse(root)
        return build(TreeNode(), 0, len(self.arr)-1)

