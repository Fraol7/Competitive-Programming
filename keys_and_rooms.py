class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True

        def dfs(k):
            for i in rooms[k]:
                if not visited[i]:
                    visited[i] = True
                    dfs(i)
        dfs(0)
        return all(visited)
