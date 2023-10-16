class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def traverse(node):
            self.visited.add(node)
            for i in graph[node]:
                if i not in self.visited:
                    self.colors[i] = not self.colors[node]
                    traverse(i)
                else:
                    if self.colors[i] == self.colors[node]:
                        self.isBiPart = False
        
        n = len(graph)
        self.isBiPart, self.visited, self.colors = True, set(), [False for _ in range(n)]
        for j in range(n):
            if j not in self.visited:
                traverse(j)
        return self.isBiPart
