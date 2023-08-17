class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        queue, visited, adj = collections.deque(), set(), [[] for _ in range(n)]
        queue.append(source)
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                if node == destination:
                    return True
                for nei in adj[node]:
                    queue.append(nei)
        
        return False
