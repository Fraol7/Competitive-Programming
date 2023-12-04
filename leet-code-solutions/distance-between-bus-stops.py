class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        tot = sum(distance)
        curr = 0
        for i in range(min(start, destination), max(start, destination)):
            curr += distance[i]
        return min(curr, tot-curr)
        