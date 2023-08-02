class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def backtrack(i, curr: List[int]):
            if i == len(graph) - 1:
                curr.append(i)
                ans.append(curr.copy())
                return
            curr.append(i)
            for j in range(len(graph[i])):
                backtrack(graph[i][j], curr)
                curr.pop()
        backtrack(0, [])
        return ans
