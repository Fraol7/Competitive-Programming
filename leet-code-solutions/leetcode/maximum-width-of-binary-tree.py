# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.refer = []
        root.val = 1
        def bfs(root, depth):
            if not root:
                return
            if len(self.refer) > depth:
                self.refer[depth].append(root.val)
            else:
                self.refer.append([root.val])
            if root.left:
                root.left.val = (root.val)*2
            if root.right:
                root.right.val = (root.val)*2 + 1
            bfs(root.left, depth+1)
            bfs(root.right, depth+1)
        bfs(root, 0)
        maxi = 0
        for i in range(len(self.refer)-1, -1, -1):
            maxi = max(maxi, self.refer[i][-1]-self.refer[i][0]+1)
        return maxi
