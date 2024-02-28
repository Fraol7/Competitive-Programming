# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        refer = {0: {0: []}}
        def helper(root, col, row, refer):
            if not root:
                return 
            if col not in refer:
                refer[col] = {}
            if row not in refer[col]:
                refer[col][row] = []
            refer[col][row].append(root.val)
            helper(root.left, col - 1, row + 1, refer)
            helper(root.right, col + 1, row + 1, refer)

        helper(root, 0, 0, refer)
        myColKeys = list(refer.keys())
        myColKeys.sort()
        arr = []
        for col in myColKeys:
            myRowKeys = list(refer[col])
            myRowKeys.sort()
            temp = []
            for row in myRowKeys:
                temp += sorted(refer[col][row])
            arr.append(temp)
        return arr
            