# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def bfs(root, depth):
            if not root:
                return
            if len(result) <= depth:
                result.append([root.val])
            else:
                result[depth].append(root.val)
            bfs(root.left, depth+1)
            bfs(root.right, depth+1)
        bfs(root, 0)
        for i in range(len(result)):
            if i%2:
                result[i] = result[i][::-1]
        return result
