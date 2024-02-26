# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        refer = defaultdict(int)
        result = []
        def helper(root):
            if not root:
                return
            refer[root.val] += 1
            helper(root.left)
            helper(root.right)
        helper(root)
        freq = max(refer.values())
        for i in refer:
            if refer[i] == freq:
                result.append(i)
        return result
        